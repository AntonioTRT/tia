from pathlib import Path
import csv

def load_words(csv_path: str):
    """Carga un CSV con columnas 'front' y 'back' y devuelve una lista de dicts.

    Si el archivo no existe devuelve lista vacía.
    """
    path = Path(csv_path)
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
