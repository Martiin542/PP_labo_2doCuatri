import pygame, random
def check_collisions(enemy_list, player_rect, lives, sound):
    """
    Verifica las colisiones entre el jugador y los enemigos, y maneja las consecuencias.

    Parámetros:
    - enemy_list (list): Una lista que almacena información de los enemigos en el juego.
    - player_rect (pygame.Rect): El rectángulo que representa la posición del jugador en la pantalla.
    - lives (int): La cantidad de vidas del jugador.
    - sound: El objeto de sonido que se reproduce en caso de colisión.

    Retorna:
    La cantidad de vidas actualizada después de verificar y manejar las colisiones.

    Esta función recorre la lista de enemigos y verifica si hay una colisión entre el jugador (representado por
    `player_rect`) y cada enemigo. Si se detecta una colisión, se elimina el enemigo de la lista, se resta una vida
    al jugador y se reproduce un sonido. Luego, se devuelve la cantidad de vidas actualizada.
    """
    for enemy in enemy_list:
        if player_rect.colliderect(enemy[1]):
            enemy_list.remove(enemy)
            lives -= 1
            sound.play()
    return lives

def check_laser_collision(laser_list, enemy_list, score, sound):
    """
    Verifica las colisiones entre los láseres y los enemigos, y maneja las consecuencias.

    Parámetros:
    - laser_list (list): Una lista que almacena información de los láseres disparados por el jugador.
    - enemy_list (list): Una lista que almacena información de los enemigos en el juego.
    - score (int): El puntaje actual del jugador.
    - sound: El objeto de sonido que se reproduce en caso de colisión.

    Retorna:
    El puntaje actualizado después de verificar y manejar las colisiones entre láseres y enemigos.

    Esta función recorre las listas de láseres y enemigos para verificar si hay colisiones entre un láser y un enemigo.
    Si se detecta una colisión, se elimina el láser, se elimina el enemigo, se aumenta el puntaje del jugador en 10 puntos
    y se reproduce un sonido. Luego, se devuelve el puntaje actualizado.
    """
    for laser in laser_list:
        for enemy in enemy_list:
            if laser.colliderect(enemy[1]):
                enemy_list.remove(enemy)
                laser_list.remove(laser)
                score += 10
                sound.play()
    return score
