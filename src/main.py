"""
Punto de entrada minimal para el proyecto de flashcards.

Ejecución: python src/main.py
"""
import sys
from pathlib import Path

from src.csv_loader import load_words

def main():
    base = Path(__file__).resolve().parents[1]
    csv_path = base / "data" / "words.csv"
    words = load_words(str(csv_path))
    print(f"Cargadas {len(words)} palabras desde {csv_path}")

if __name__ == "__main__":
    main()
