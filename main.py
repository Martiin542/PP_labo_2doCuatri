import pygame, random, json
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
laser_sound = pygame.mixer.Sound('assets\\laser_sound.mp3')
laser_sound.set_volume(0.3)
enemy_kill_sound = pygame.mixer.Sound('assets\\hit_sound.mp3')
enemy_kill_sound.set_volume(0.3)
collision_sound = pygame.mixer.Sound('assets\\colision_sound.mp3')
collision_sound.set_volume(0.3)

#player
player_image = pygame.image.load('assets\\spaceship.png')
width, heigth = player_image.get_size()
new_width = int(width * 0.15)
new_height = int(heigth * 0.15)
scaled_img = pygame.transform.scale(player_image, (new_width, new_height))
player_rect = scaled_img.get_rect()
player_rect.topleft = (SCREEN_W/2 - 50, SCREEN_H - 100)
player_speed = 6
move_right = False
move_left = False
move_up = False
move_down = False
lives = 3
score = 0
lasers = []
is_firing = False
laser_width = 3
laser_height = 15

#enemy
enemies = []
enemy_images = [
    pygame.image.load('assets\\green.png'),
    pygame.image.load('assets\\red.png'),
    pygame.image.load('assets\\yellow.png')
]
def create_enemy():
    enemy_image = random.choice(enemy_images)
    width, height = enemy_image.get_size()
    new_width = int(width * 1)
    new_height = int(height * 1)
    scaled_img = pygame.transform.scale(enemy_image, (new_width, new_height))
    enemy_rect = scaled_img.get_rect()
    enemy_rect.topleft = (random.randint(0, SCREEN_W - enemy_rect.width), 0)
    enemy_speed = 2
    enemies.append((scaled_img, enemy_rect, enemy_speed))

def move_enemies():
    global score
    for enemy in enemies:
        enemy[1].y += enemy[2]
        if enemy[1].top > SCREEN_H:
            enemies.remove(enemy)
            score -= 10

def check_collisions():
    global lives
    for enemy in enemies:
        if player_rect.colliderect(enemy[1]):
            enemies.remove(enemy)
            lives -= 1
            collision_sound.play()

def check_laser_collision():
    global score
    for laser in lasers:
        for enemy in enemies:
            if laser.colliderect(enemy[1]):
                enemies.remove(enemy)
                lasers.remove(laser)
                score += 10
                enemy_kill_sound.play()

def restart_game():
    global lives, score, player_rect, lasers, enemies, game_over
    lives = 3
    score = 0
    player_rect.topleft = (SCREEN_W/2 - 50, SCREEN_H - 100)
    lasers = []
    enemies = []
    game_over = False

#score
def load_max_score():
    try:
        with open('max_score.json', 'r') as file:
            data = json.load(file)
            return data["max_score"]
    except FileNotFoundError:
        return 0

def save_max_score(max_score):
    data = {"max_score": max_score}
    with open('max_score.json', 'w') as file:
        json.dump(data, file)

max_score = load_max_score()

#power up:

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
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
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
    elif game_over == True:
        label(screen, 400, 0,'assets\labelgameover.png', 2)
        draw_text(screen, f'Final Score: {score}', font, TEXT_COL, 0,300)
        restart_button = button(screen, SCREEN_W/2 - 60, SCREEN_H/2, 'assets\\restart_button.png', 1)
        if restart_button:
            restart_game()
    #juego
    else:
        screen.blit(background_image_game, (0,0))

        if move_right:
            player_rect.x += player_speed
            if player_rect.right > SCREEN_W:
                player_rect.right = SCREEN_W
        if move_left:
            player_rect.x -= player_speed
            if player_rect.left < 0:
                player_rect.left = 0
        if move_up:
            player_rect.y -= player_speed
            if player_rect.top < 0:
                player_rect.top = 0
        if move_down:
            player_rect.y += player_speed
            if player_rect.bottom > SCREEN_H:
                player_rect.bottom = SCREEN_H
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE] and not is_firing: 
            laser = pygame.Rect(player_rect.centerx - laser_width // 2, player_rect.top, laser_width, laser_height)
            lasers.append(laser)
            is_firing = True
            laser_sound.play()
        if not keys[pygame.K_SPACE]:
            is_firing = False

        for laser in lasers:
            laser.y -= 5
            pygame.draw.rect(screen, (255, 0, 0), laser)

        screen.blit(scaled_img, player_rect.topleft)

        if score > max_score:
            max_score = score
            save_max_score(max_score)

        draw_text(screen, f'Max Score: {max_score}', font, TEXT_COL, SCREEN_W // 2 - 100, 10)
        draw_text(screen, f'Lives: {lives}', font, TEXT_COL, 0,0)
        draw_text(screen, f'Score: {score}', font, TEXT_COL, 0,40)
        if lives <= 0:
            game_over = True

        move_enemies()
        check_collisions()
        check_laser_collision()
        if random.randint(0, 100) < 2:  
            create_enemy()
        for enemy in enemies:
            screen.blit(enemy[0], enemy[1])

    pygame.display.update()

pygame.quit()
