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
from PyQt5.QtWidgets import QApplication
sys.path.append(os.path.dirname(__file__))
from ui import FlashcardApp


# Main function to launch only the PyQt UI
def main():
    app = QApplication(sys.argv)
    window = FlashcardApp()
    window.show()
    sys.exit(app.exec_())

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
