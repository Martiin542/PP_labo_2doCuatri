import pygame, json
def load_max_score():
    """
    Carga el puntaje máximo almacenado en un archivo JSON.

    Retorna:
    El puntaje máximo cargado desde el archivo JSON, o 0 si el archivo no existe.
    """
    try:
        with open('max_score.json', 'r') as file:
            data = json.load(file)
            return data["max_score"]
    except FileNotFoundError:
        return 0

def save_max_score(max_score):
    """
    Guarda el puntaje máximo en un archivo JSON.

    Parámetros:
    - max_score (int): El puntaje máximo que se desea guardar en el archivo.

    Retorna:
    Ninguno (None)
    """
    data = {"max_score": max_score}
    try:
        with open('max_score.json', 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error al guardar el puntaje máximo: {e}")