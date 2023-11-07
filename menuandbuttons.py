import pygame

def button(screen, x, y, image, scale):
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
    image = pygame.image.load(image).convert_alpha()
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    rect = image.get_rect()
    rect.topleft = (x, y)

    screen.blit(image, (rect.x, rect.y))


