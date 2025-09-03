import sys
import requests
import html
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox


class QuizApp(QWidget):
    def __init__(self, difficulty="easy", num_questions=5):
        super().__init__()

        self.setWindowTitle("Quiz")
        self.setGeometry(200, 200, 600, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.questions = self.get_questions(difficulty, num_questions)
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)

        self.score_label = QLabel(f"Acertos: {self.score}/{self.total_questions}")
        self.layout.addWidget(self.score_label)

        self.question_label = QLabel("")
        self.question_label.setWordWrap(True)
        self.layout.addWidget(self.question_label)

        self.answer_buttons = []
        for i in range(4):
            btn = QPushButton("")
            btn.clicked.connect(self.check_answer)
            self.layout.addWidget(btn)
            self.answer_buttons.append(btn)
        
        self.skip_button = QPushButton("Pular questão")
        self.skip_button.clicked.connect(self.skip_question)
        self.layout.addWidget(self.skip_button)

        self.load_question()
    def skip_question(self):
        self.current_question += 2  # Pula duas questões em vez de uma
        self.load_question()

    def get_questions(self, difficulty, num_questions):
        # Mapear dificuldades em português para inglês
        difficulty_map = {
            "facil": "easy",
            "medio": "medium", 
            "dificil": "hard"
        }
        api_difficulty = difficulty_map.get(difficulty, difficulty)
        
        url = f"https://opentdb.com/api.php?amount={num_questions}&type=multiple&difficulty={api_difficulty}"
        response = requests.get(url)
        data = response.json()
        questions = []

        for item in data["results"]:
            question = html.unescape(item["question"])
            correct = html.unescape(item["correct_answer"])
            incorrect = [html.unescape(ans) for ans in item["incorrect_answers"]]
            options = incorrect + [correct]
            random.shuffle(options)

            questions.append({
                "question": question,
                "correct": correct,
                "options": options
            })
        return questions

    def load_question(self):
        if self.current_question < self.total_questions:
            q = self.questions[self.current_question]
            self.question_label.setText(q["question"])
            for i, option in enumerate(q["options"]):
                self.answer_buttons[i].setText(option)
                self.answer_buttons[i].setEnabled(True)
        else:
            self.show_result()

    def check_answer(self):
        clicked_button = self.sender()
        answer = clicked_button.text()
        correct = self.questions[self.current_question]["correct"]

        if answer == correct:
            self.score += 1

        self.current_question += 1

        self.score_label.setText(f"Acertos: {self.score}/{self.total_questions}")

        self.load_question()

    def show_result(self):
        QMessageBox.information(
            self,
            "Resultado",
            f"Você acertou {self.score} de {self.total_questions} questões!"
        )
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz = QuizApp("medium", 5)
    quiz.show()
    sys.exit(app.exec_())
