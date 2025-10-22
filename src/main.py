def main():
    app = QApplication(sys.argv)
    window = FlashcardApp()
    window.show()
    sys.exit(app.exec_())

"""
Minimal entry point for the flashcard project.

Run: python src/main.py
"""




import sys
import os
import csv
import random
from PyQt5.QtWidgets import QApplication
sys.path.append(os.path.dirname(__file__))
from ui import FlashcardApp



# Main function to launch the PyQt UI and handle all logic
def main():
    app = QApplication(sys.argv)
    window = FlashcardApp()

    # Load all words from CSV

    try:
        with open('data/words.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            # Each word is a dict: {'A': ..., 'B': ..., 'count': 0}
            words = [
                {'A': row[0], 'B': row[1], 'count': 0}
                for row in rows[1:] if row and len(row) >= 2
            ]
    except Exception as e:
        words = []
        window.label.setText(f'Error loading CSV: {e}')

    state = {
        'words': words,  # List of dicts
        'current_word': None,
        'current_answer': None,
        'score': 0,
        'lang': 'AtoB',  # 'AtoB' means show A and expect B, 'BtoA' is the reverse
        'current_entry': None,  # The dict for the current word
    }

    def show_new_word():
        # Only show words that have not been answered correctly 3 times
        available = [w for w in state['words'] if w['count'] < 3]
        if not available:
            window.label.setText('All done! You mastered all words!')
            window.input.setDisabled(True)
            window.button.setDisabled(True)
            window.check_button.setDisabled(True)
            window.switch_lang_button.setDisabled(True)
            return
        word = random.choice(available)
        state['current_entry'] = word
        if state['lang'] == 'AtoB':
            state['current_word'] = word['A']
            state['current_answer'] = word['B']
            window.label.setText(f'Word: {state["current_word"]}')
        else:
            state['current_word'] = word['B']
            state['current_answer'] = word['A']
            window.label.setText(f'Word: {state["current_word"]}')
        window.input.clear()
        window.feedback.setText('')

    def check_answer():
        user_input = window.input.text().strip().lower()
        correct = (state['current_answer'] or '').strip().lower()
        if user_input == correct:
            window.feedback.setText(f'OK! The answer is: {state["current_answer"]}')
            state['score'] += 1
            # Increment correct count for this word
            if state['current_entry']:
                state['current_entry']['count'] += 1
        else:
            window.feedback.setText(f'Not OK. The correct answer is: {state["current_answer"]}')
        window.score_label.setText(f'Score: {state["score"]}')
        # Show a new word after checking
        show_new_word()

    def switch_language():
        if state['lang'] == 'AtoB':
            state['lang'] = 'BtoA'
            window.switch_lang_button.setText('Switch to A → B')
        else:
            state['lang'] = 'AtoB'
            window.switch_lang_button.setText('Switch to B → A')
        show_new_word()


    # Connect UI button signals directly to logic
    window.button.clicked.disconnect()
    window.button.clicked.connect(show_new_word)
    window.check_button.clicked.disconnect()
    window.check_button.clicked.connect(check_answer)
    window.switch_lang_button.clicked.disconnect()
    window.switch_lang_button.clicked.connect(switch_language)

    # Set initial state
    state['words'] = words
    show_new_word()

    window.show()
    sys.exit(app.exec_())

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
