from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton

class OpcoesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opções")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Dificuldade:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["easy", "medium", "hard"])
        layout.addWidget(self.difficulty_combo)

        layout.addWidget(QLabel("Número de perguntas:"))
        self.num_questions_spin = QSpinBox()
        self.num_questions_spin.setRange(1, 20)  
        self.num_questions_spin.setValue(5)    
        layout.addWidget(self.num_questions_spin)


        self.save_button = QPushButton("Salvar")
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def get_options(self):
        return {
            "difficulty": self.difficulty_combo.currentText(),
            "num_questions": self.num_questions_spin.value()
        }
