import pygame

def button(screen, x, y, image, scale):
    """
    Crea un botón gráfico en una superficie de pantalla.

    Parámetros:
    - screen (pygame.Surface): La superficie de pantalla en la que se dibujará el botón.
    - x (int): La coordenada x de la esquina superior izquierda del botón.
    - y (int): La coordenada y de la esquina superior izquierda del botón.
    - image (str): La ruta de la imagen que se utilizará como apariencia del botón.
    - scale (float): El factor de escala para redimensionar la imagen del botón.

    Retorna:
    Un valor booleano (clicked) que indica si el botón ha sido clickeado o no.

    Esta función crea un botón gráfico en la superficie de pantalla especificada en las coordenadas (x, y)
    utilizando una imagen dada. El botón puede ser clickeado y el estado de clickeo se devuelve como `clicked`.
    """
    image = pygame.image.load(image)
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    rect = image.get_rect()
    rect.topleft = (x, y)
    clicked = False

    mouse_pos = pygame.mouse.get_pos()

    if rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
    
    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False
    
    screen.blit(image, (rect.x, rect.y))

    return clicked

def label(screen, x, y, image, scale):
    """
    Muestra una etiqueta gráfica en una superficie de pantalla.

    Parámetros:
    - screen (pygame.Surface): La superficie de pantalla en la que se mostrará la etiqueta.
    - x (int): La coordenada x de la esquina superior izquierda de la etiqueta.
    - y (int): La coordenada y de la esquina superior izquierda de la etiqueta.
    - image (str): La ruta de la imagen que se utilizará como etiqueta.
    - scale (float): El factor de escala para redimensionar la imagen de la etiqueta.

    Retorna:
    Ninguno (None).

    Esta función carga una imagen dada, la redimensiona según el factor de escala proporcionado y la coloca
    en la superficie de pantalla en las coordenadas especificadas (x, y). La etiqueta se muestra en la pantalla.
    """
    image = pygame.image.load(image).convert_alpha()
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    rect = image.get_rect()
    rect.topleft = (x, y)

    screen.blit(image, (rect.x, rect.y))


