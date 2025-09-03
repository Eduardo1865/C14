import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from opcoes import OpcoesWindow
from jogo import QuizApp

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("quiz")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("quiz!")
        layout.addWidget(self.label)

        self.start_button = QPushButton("iniciar quiz")
        self.options_button = QPushButton("opções")
        layout.addWidget(self.start_button)
        layout.addWidget(self.options_button)

        self.setLayout(layout)

        self.options = {
            "difficulty": "medium",
            "num_questions": 10
        }

        self.options_button.clicked.connect(self.open_options)
        self.start_button.clicked.connect(self.start_quiz)

    def open_options(self):
        self.opcoes_window = OpcoesWindow()
        self.opcoes_window.show()
        self.opcoes_window.save_button.clicked.connect(self.save_options)

    def save_options(self):
        self.options = self.opcoes_window.get_options()
        print("Opções salvas:", self.options)
        self.opcoes_window.close()

    def start_quiz(self):
        self.quiz_window = QuizApp(
            difficulty=self.options["difficulty"],
            num_questions=self.options["num_questions"]
        )
        self.quiz_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())
