import pygame, math
from gen_functions import draw_text
from menuandbuttons import button, label

pygame.init()
pygame.mixer.init() 

clock = pygame.time.Clock()
FPS = 60

SCREEN_W = 1240
SCREEN_H = 924

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Juego Basico')

#textos
font = pygame.font.SysFont('arialblack', 40)
TEXT_COL = (255,255,255)

#fondo & musica menu
background_image = pygame.image.load('assets\\backmenu.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_W, SCREEN_H))
menu_music = 'assets\\menu_music.mp3'
music_muted = False

#fondo & musica juego
background_image_game = pygame.image.load('assets\\backgame.jpg')
background_image_game = pygame.transform.scale(background_image_game, (SCREEN_W, SCREEN_H))

#player
def create_player(img_path, x, y, scale, speed):
    player_image = pygame.image.load(img_path)
    width, heigth = player_image.get_size()
    new_width = int(width * scale)
    new_height = int(heigth * scale)
    scaled_img = pygame.transform.scale(player_image, (new_width, new_height))
    player_rect = scaled_img.get_rect()
    player_rect.topleft = (x, y)
    player_speed = speed
    return scaled_img, player_rect, player_speed
player_img, player_rect, player_speed = create_player('assets\\spaceship.png', 100, 100, 0.25, 10)
move_right = False
move_left = False
move_up = False
move_down = False


#estados del juego
main_menu = True
game_paused = False
game_over = False

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
    
    screen.fill((52, 78, 91))

    #menu
    if main_menu == True:
        #musica
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(menu_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1) 
        #botones y screen
        screen.blit(background_image, (0,0))
        titulo_in_game = label(screen, 150, 50, 'assets\\labelingame.png', 1)
        play = button(screen, SCREEN_W/2 - 60, SCREEN_H/2, 'assets\\play_button.png', 1)
        exit = button(screen, SCREEN_W/2 - 58, SCREEN_H/2+100, 'assets\\exit_button.png', 1)
        mute_music = button(screen, 5, SCREEN_H-65, 'assets\\mute_button.png', 1)
        if play:
            main_menu = False
        if exit:
            run = False
        if mute_music and music_muted == False:
            music_muted = True
        elif mute_music == True and music_muted == True:
            music_muted = False
        if music_muted:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.unpause()
    #pausa        
    elif game_paused == True: 
        pass
    #juego
    else:
        screen.blit(background_image_game, (0,0))
        screen.blit(player_img, player_rect.topleft)

        if move_right:
            player_rect.x += player_speed
        if move_left:
            player_rect.x -= player_speed
        if move_up:
            player_rect.y -= player_speed
        if move_down:
            player_rect.y += player_speed
        


    pygame.display.update()

pygame.quit()
