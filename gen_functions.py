import pygame

SCREEN_W = 1240
SCREEN_H = 924

def draw_text(screen, text, font, text_col, x, y):
    """
    Dibuja texto en una superficie de pantalla con la fuente y color especificados.
    Parámetros:
    - screen (pygame.Surface): La superficie de pantalla en la que se dibujará el texto.
    - text (str): El texto que se desea mostrar en la pantalla.
    - font (pygame.font.Font): La fuente que se utilizará para renderizar el texto.
    - text_col (tuple): El color del texto representado como una tupla (R, G, B) o (R, G, B, A).
    - x (int): La coordenada x en la que se dibujará el texto en la superficie de pantalla.
    - y (int): La coordenada y en la que se dibujará el texto en la superficie de pantalla.

    Retorna:
    Ninguno (None)

    Esta función renderiza el texto en la fuente especificada y lo coloca en la posición (x, y)
    en la superficie de pantalla, utilizando el color de texto proporcionado.
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def restart_game(lives, score, player_rect, lasers, enemies, game_over):
    """
    Reinicia los valores del juego, vidas, puntaje, posición del jugador, y más.

    Parámetros:
    - lives (int): La cantidad de vidas que el jugador tiene.
    - score (int): El puntaje actual del jugador.
    - player_rect (pygame.Rect): El rectángulo que representa la posición del jugador en la pantalla.
    - lasers (list): Una lista que contiene los láseres disparados por el jugador.
    - enemies (list): Una lista que contiene los enemigos en el juego.
    - game_over (bool): Un booleano que indica si el juego ha terminado.

    Retorna:
    Una tupla que contiene los valores reiniciados de lives, score, player_rect, lasers, enemies y game_over.

    Esta función reinicia los valores del juego, configurando las vidas a 3, el puntaje a 0, la posición del jugador
    en un lugar predefinido, y vaciando las listas de láseres y enemigos. El estado del juego se establece en False
    indicando que no ha terminado.
    """
    lives = 3
    score = 0
    player_rect.topleft = (SCREEN_W/2 - 50, SCREEN_H - 100)
    lasers = []
    enemies = []
    game_over = False

    return lives, score, player_rect, lasers, enemies, game_over