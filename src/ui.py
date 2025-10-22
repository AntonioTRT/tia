
# Import necessary PyQt5 widgets and modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys


# Main window for the flashcard application
import csv
import random

class FlashcardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Flashcards')  # Set window title
        self.layout = QVBoxLayout()        # Create vertical layout
        self.label = QLabel('Word:')       # Label to show the word
        self.input = QLineEdit()           # Input field for the answer
        self.button = QPushButton('Nueva palabra')  # Button for new word
        self.check_button = QPushButton('Check')    # Button to check answer
        self.feedback = QLabel('')         # Label to show feedback
        self.score_label = QLabel('Score: 0') # Label to show score
        # Add widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.check_button)
        self.layout.addWidget(self.feedback)
        self.layout.addWidget(self.score_label)
        self.setLayout(self.layout)       # Set the layout for the window

        # Load all words from CSV
        self.words = self.load_words('data/words.csv')
        self.current_word = None
        self.current_answer = None
        self.score = 0

        # Connect buttons
        self.button.clicked.connect(self.show_new_word)
        self.check_button.clicked.connect(self.check_answer)

        # Show the first word
        self.show_new_word()

    def load_words(self, file):
        words = []
        try:
            with open(file, encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                words = [row for row in rows[1:] if row]
        except Exception as e:
            self.feedback.setText(f'Error loading CSV: {e}')
        return words

    def show_new_word(self):
        if not self.words:
            self.label.setText('No words loaded')
            return
        word = random.choice(self.words)
        self.current_word = word[0]
        self.current_answer = word[1]
        self.label.setText(f'Word: {self.current_word}')
        self.input.clear()
        self.feedback.setText('')

    def check_answer(self):
        user_input = self.input.text().strip().lower()
        correct = self.current_answer.strip().lower()
        if user_input == correct:
            self.feedback.setText(f'OK! The answer is: {self.current_answer}')
            self.score += 1
        else:
            self.feedback.setText(f'Not OK. The correct answer is: {self.current_answer}')
        self.score_label.setText(f'Score: {self.score}')

# Run the UI if this file is executed directly
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlashcardApp()
    window.show()
    sys.exit(app.exec_())
