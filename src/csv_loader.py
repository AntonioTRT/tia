def loader_word(file):
    with open(file, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    palabras = [row for row in rows[1:] if row]
    palabra = random.choice(palabras)
    pregunta = palabra[0]
    respuesta = palabra[1]
    user_input = input(f"....: {pregunta}\n> ")
    print(f"x: {pregunta}  y: {user_input}")
    if user_input.strip().lower() == respuesta.strip().lower():
        print("ok")
    else:
        print(f"not OK: {respuesta}")
import csv
import random

# Function to load a random word from a CSV file and check user input
def loader_word(file):
    # Open the CSV file
    with open(file, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Skip the header and filter out empty rows
    palabras = [row for row in rows[1:] if row]
    # Choose a random word
    palabra = random.choice(palabras)
    pregunta = palabra[0]  # The word to prompt
    respuesta = palabra[1]  # The correct answer
    # Ask the user for input
    user_input = input(f"....: {pregunta}\n> ")
    # Show the prompt and the user's answer
    print(f"x: {pregunta}  y: {user_input}")
    # Check if the answer is correct (case-insensitive)
    if user_input.strip().lower() == respuesta.strip().lower():
        print("ok")
    else:
        print(f"not OK: {respuesta}")

# Run the loader_word function if this file is executed directly
if __name__ == "__main__":
    loader_word("data/words.csv")