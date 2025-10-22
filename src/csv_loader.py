import csv
import random

file = "data/words.csv"

def loader_word():
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

if __name__ == "__main__":
    loader_word()