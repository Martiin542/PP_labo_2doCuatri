import pygame, random

SCREEN_W = 1240
SCREEN_H = 924

def create_enemy(enemy_list, img_path):
    """
    Crea un enemigo y lo agrega a una lista de enemigos en el juego.

    Parámetros:
    - enemy_list (list): Una lista que almacena información de los enemigos en el juego.
    - img_path (list): Una lista de rutas de imágenes desde las cuales se selecciona al azar la imagen del enemigo.

    Retorna:
    Ninguno (None).

    Esta función selecciona una imagen al azar de las rutas proporcionadas en `img_path`, redimensiona la imagen,
    coloca el enemigo en una posición aleatoria en la parte superior de la pantalla y lo agrega a la lista de enemigos
    junto con su velocidad.
    """
    enemy_image = random.choice(img_path)
    width, height = enemy_image.get_size()
    new_width = int(width * 1)
    new_height = int(height * 1)
    scaled_img = pygame.transform.scale(enemy_image, (new_width, new_height))
    enemy_rect = scaled_img.get_rect()
    enemy_rect.topleft = (random.randint(0, SCREEN_W - enemy_rect.width), 0)
    enemy_speed = 2
    enemy_list.append((scaled_img, enemy_rect, enemy_speed))

def move_enemies(enemy_list, score):
    """
    Mueve los enemigos hacia abajo en la pantalla y maneja su eliminación.

    Parámetros:
    - enemy_list (list): Una lista que almacena información de los enemigos en el juego.
    - score (int): El puntaje actual del jugador.

    Retorna:
    El puntaje actualizado después de mover y eliminar enemigos.

    Esta función recorre la lista de enemigos y mueve cada enemigo hacia abajo en la pantalla. Si un enemigo
    se encuentra por debajo del borde inferior de la pantalla, se elimina de la lista de enemigos y se reduce
    el puntaje del jugador en 10 puntos.
    """
    try:
        for enemy in enemy_list:
            enemy[1].y += enemy[2]
            if enemy[1].top > SCREEN_H:
                enemy_list.remove(enemy)
                score -= 10
    except Exception as e:
        print(f"Error en la manipulación de la lista de enemigos: {e}")
    return score