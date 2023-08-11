'''
Данная работа была выполнена для 7 лабы Кодифая
Работу сделали Асаналиев Доолот и Болотбеков Тимур
Просьба настроить все пути в коде или создать такие же
пути которые написаны в коде
'''
import pygame
'''
Сначала создаем необходимые переменные
которыми мы и будем пользоваться в коде
начиная от надпискй заканчивая самими персонажами
'''
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1510, 830)) # flags=pygame.NOFRAME, Убирает рамки
pygame.display.set_caption("UFO'S WAR")

icon = pygame.image.load("VS code/Images/UFO.png").convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load("VS code/Images/bg.png").convert()
bg_y = 0
bg_sound = pygame.mixer.Sound('VS code/Music/bg_sound.mp3')
bg_sound.play(-1)

myfont = pygame.font.Font('VS code/fonts/REM-Medium.ttf', 100)
myfont1 = pygame.font.Font('VS code/fonts/REM-Medium.ttf', 85)
myfont2 = pygame.font.Font('VS code/fonts/REM-Medium.ttf', 45)
Welcome_text = myfont.render("Welcome to UFO'S WAR", True, (176, 176, 23))
Play_text = myfont1.render('Play', True, (242, 72, 53))
Settings_text = myfont1.render('Settings', True, (242, 72, 53))
Quit_text = myfont1.render('Quit', True, (242, 72, 53))
Choose_game_speed_text = myfont1.render('Choose game speed:', True, (242, 72, 53))
game_speed_text1 = myfont1.render('0.5X', True, (242, 72, 53))
game_speed_text2 = myfont1.render('1X', True, (242, 72, 53))
game_speed_text3 = myfont1.render('1.5X', True, (242, 72, 53))
game_speed_text4 = myfont1.render('2X', True, (242, 72, 53))
Back_text = myfont2.render('Back', True, (242, 72, 53))
player1_winner_text = myfont.render("PLAYER #1 WIN!", True, (242,72,53))
player2_winner_text = myfont.render("PLAYER #2 WIN!", True, (242,72,53))
Play_again_text = myfont2.render('Play again', True, (242, 72, 53))
Main_menu_text = myfont2.render('Main menu', True, (242, 72, 53))
Draw_text = myfont.render('Draw', True, (242, 72, 53))

player1 = pygame.image.load('VS code/Images/Characters/Bottom2.png').convert_alpha()
player2 = pygame.image.load('VS code/Images/Characters/Top3.png').convert_alpha()
bullet1 = pygame.image.load('VS code/Images/bullet_bottom.png').convert_alpha()
bullet2 = pygame.image.load('VS code/Images/bullet_top.png').convert_alpha()
full_hp = pygame.image.load('VS code/Images/full_hp1.png').convert_alpha()

running = True
before_playing = True
gameplay = False
after_playing = False

Welcome_text_x = 150
Welcome_text_y = 50
Play_text_x = 650
Play_text_y = 250
Settings_text_x = 580
Settings_text_y = 400
Quit_text_x = 645
Quit_text_y = 550
Language_text_x = 100
Language_text_y = 700
Choose_game_speed_text_x = 10000
Choose_game_speed_text_y = 10000
game_speed_text1_x = 10000
game_speed_text1_y = 10000
game_speed_text2_x = 10000
game_speed_text2_y = 10000
game_speed_text3_x = 10000
game_speed_text3_y = 10000
game_speed_text4_x = 10000
game_speed_text4_y = 10000
Back_text_x = 10000
Back_text_y = 10000
player_speed = 10
player2_x = 700
player2_y = 50
player1_x = 700
player1_y = 720
full_hp2_x = 50
full_hp3_x = 100
full_hp2_y = 770
full_hp3_y = 770
player1_life = 3
player2_life = 3

bullet_timer1 = pygame.USEREVENT + 1
bullet_timer2 = pygame.USEREVENT + 1
pygame.time.set_timer(bullet_timer2, 750)
pygame.time.set_timer(bullet_timer1, 750)
bullet_list_in_game1 = []
bullet_list_in_game2 = []

Time30 = False
Time40 = True
Time60 = False
Time80 = False
'''
Дальше после создания необходимых переменных
идет основной цикл while где и будут происходить
все процессы игры
'''
while running:
    if Time30 and not Time40 and not Time60 and not Time80:
        clock.tick(30)
    if Time40 and not Time30 and not Time60 and not Time80:
        clock.tick(40)
    if Time60 and not Time40 and not Time30 and not Time80:
        clock.tick(60)
    if Time80 and not Time40 and not Time60 and not Time30:
        clock.tick(80)
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y + 830))
    bg_y -= 2
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    player1_rect = player1.get_rect(topleft=(player1_x, player1_y))
    player2_rect = player2.get_rect(topleft=(player2_x, player2_y))
    if bg_y == -830:
        bg_y = 0
    if not gameplay and before_playing:
        screen.blit(Welcome_text, (Welcome_text_x, Welcome_text_y))
        screen.blit(Play_text, (Play_text_x, Play_text_y))
        screen.blit(Settings_text, (Settings_text_x, Settings_text_y))
        screen.blit(Quit_text, (Quit_text_x, Quit_text_y))
        screen.blit(Choose_game_speed_text, (Choose_game_speed_text_x, Choose_game_speed_text_y))
        screen.blit(game_speed_text1, (game_speed_text1_x, game_speed_text1_y))
        screen.blit(game_speed_text2, (game_speed_text2_x, game_speed_text2_y))
        screen.blit(game_speed_text3, (game_speed_text3_x, game_speed_text3_y))
        screen.blit(game_speed_text4, (game_speed_text4_x, game_speed_text4_y))
        screen.blit(Back_text, (Back_text_x, Back_text_y))
        play_text_rect = Play_text.get_rect(topleft=(Play_text_x, Play_text_y))
        quit_text_rect = Quit_text.get_rect(topleft=(Quit_text_x, Quit_text_y))
        game_speed1_rect = game_speed_text1.get_rect(topleft=(game_speed_text1_x, game_speed_text1_y))
        game_speed2_rect = game_speed_text2.get_rect(topleft=(game_speed_text2_x, game_speed_text2_y))
        game_speed3_rect = game_speed_text3.get_rect(topleft=(game_speed_text3_x, game_speed_text3_y))
        game_speed4_rect = game_speed_text4.get_rect(topleft=(game_speed_text4_x, game_speed_text4_y))
        settings_text_rect = Settings_text.get_rect(topleft=(Settings_text_x, Settings_text_y))
        back_text_rect = Back_text.get_rect(topleft=(Back_text_x, Back_text_y))
        main_menu_rect = Main_menu_text.get_rect(topleft=(850, 400))
        play_again_rect = Play_again_text.get_rect(topleft=(350, 400))
    if gameplay and not before_playing and not after_playing:
        screen.blit(player1, (player1_x, player1_y))
        screen.blit(player2, (player2_x, player2_y))
        screen.blit(full_hp, (0, 0))
        screen.blit(full_hp, (full_hp2_x, 0))
        screen.blit(full_hp, (full_hp3_x, 0))
        screen.blit(full_hp, (0, 770))
        screen.blit(full_hp, (50, full_hp2_y))
        screen.blit(full_hp, (100, full_hp3_y))
        if player2_life == 2:
            full_hp3_x = 10000
        if player2_life == 1:
            full_hp2_x = 10000
        if player1_life == 2:
            full_hp3_y = 10000
        if player1_life == 1:
            full_hp2_y = 10000
        if bullet_list_in_game1:
            for (i, el) in enumerate(bullet_list_in_game1):
                screen.blit(bullet1, el)
                el.y -= 5
                if el.y < -10:
                    bullet_list_in_game1.pop(i)
                if player2_rect.colliderect(el):
                    bullet_list_in_game1.pop(i)
                    player2_life -= 1
                    if player2_life == 0 and player1_life > 0:
                        gameplay = False
                        after_playing = True
        if bullet_list_in_game2:
            for (i, el) in enumerate(bullet_list_in_game2):
                screen.blit(bullet2, el)
                el.y += 5
                if el.y > 840:
                    bullet_list_in_game2.pop(i)
                if player1_rect.colliderect(el):
                    bullet_list_in_game2.pop(i)
                    player1_life -= 1
                    if player1_life == 0 and player2_life > 0:
                        gameplay = False
                        after_playing = True
        if keys[pygame.K_LEFT] and player1_x > 100:
            player1_x -= player_speed
        if keys[pygame.K_RIGHT] and player1_x < 1410:
            player1_x += player_speed
        if keys[pygame.K_UP] and player1_y > 550:
            player1_y -= player_speed
        if keys[pygame.K_DOWN] and player1_y < 765:
            player1_y += player_speed
        if keys[pygame.K_a] and player2_x > 100:
            player2_x -= player_speed
        if keys[pygame.K_d] and player2_x < 1410:
            player2_x += player_speed
        if keys[pygame.K_w] and player2_y > 5:
            player2_y -= player_speed
        if keys[pygame.K_s] and player2_y < 345:
            player2_y += player_speed
    if after_playing and not gameplay:
        bullet_list_in_game1.clear()
        bullet_list_in_game2.clear()
        if player1_life == 0 and player2_life > 0:
            screen.blit(player2_winner_text, (300, 200))
        if player2_life == 0 and player1_life > 0:
            screen.blit(player1_winner_text, (300, 200))
        if player1_life == 0 and player2_life == 0:
            screen.blit(Draw_text, (600, 200))
        screen.blit(Play_again_text, (350, 400))
        screen.blit(Main_menu_text, (850, 400))
        player1_x = 10000
        player1_y = 10000
        player2_x = 10000
        player2_y = 10000
        
    '''
    Все эти иксы, игрики нужны для обозначения позиций надписей
    что бы их можно было перетаскивать во время нажатия чего либо
    '''
    '''
    Дальше идет обработчик событий для работы мыши с кнопками/текстами
    да и в целом все события которые будут происходить будут обрабатываться
    в данном цикле
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_text_rect.collidepoint(mouse):
                before_playing = False
                gameplay = True
                after_playing = False
                player2_x = 700
                player2_y = 50
                player1_x = 700
                player1_y = 720
                player1_life = 3
                player2_life = 3
                full_hp2_x = 50
                full_hp3_x = 100
                full_hp2_y = 770
                full_hp3_y = 770
            if quit_text_rect.collidepoint(mouse):
                pygame.quit()
            if settings_text_rect.collidepoint(mouse):
                Welcome_text_x = 10000
                Welcome_text_y = 10000
                Play_text_x = 10000
                Play_text_y = 10000
                Settings_text_x = 10000
                Settings_text_y = 10000
                Quit_text_x = 10000
                Quit_text_y = 10000
                Language_text_x = 10000
                Language_text_y = 10000
                Choose_game_speed_text_x = 350
                Choose_game_speed_text_y = 100
                Back_text_x = 50
                Back_text_y = 750
                game_speed_text1_x = 360
                game_speed_text1_y = 250
                game_speed_text2_x = 600
                game_speed_text2_y = 250
                game_speed_text3_x = 770
                game_speed_text3_y = 250
                game_speed_text4_x = 1035
                game_speed_text4_y = 250
            if back_text_rect.collidepoint(mouse):
                Welcome_text_x = 150
                Welcome_text_y = 50
                Play_text_x = 650
                Play_text_y = 250
                Settings_text_x = 580
                Settings_text_y = 400
                Quit_text_x = 645
                Quit_text_y = 550
                Language_text_x = 100
                Language_text_y = 700
                Choose_game_speed_text_x = 10000
                Choose_game_speed_text_y = 10000
                game_speed_text1_x = 10000
                game_speed_text1_y = 10000
                game_speed_text2_x = 10000
                game_speed_text2_y = 10000
                game_speed_text3_x = 10000
                game_speed_text3_y = 10000
                game_speed_text4_x = 10000
                game_speed_text4_y = 10000
                Back_text_x = 10000
                Back_text_y = 10000
            if game_speed1_rect.collidepoint(mouse):
                Time30 = True
                Time40 = False
                Time60 = False
                Time80 = False
            if game_speed2_rect.collidepoint(mouse):
                Time40 = True
                Time30 = False
                Time60 = False
                Time80 = False
            if game_speed3_rect.collidepoint(mouse):
                Time60 = True
                Time40 = False
                Time30 = False
                Time80 = False
            if game_speed4_rect.collidepoint(mouse):
                Time80 = True
                Time30 = False
                Time40 = False
                Time60 = False
            if play_again_rect.collidepoint(mouse):
                gameplay = True
                after_playing = False
                before_playing = False
                player2_x = 700
                player2_y = 50
                player1_x = 700
                player1_y = 720
                player1_life = 3
                player2_life = 3
                full_hp2_x = 50
                full_hp3_x = 100
                full_hp2_y = 770
                full_hp3_y = 770
            if main_menu_rect.collidepoint(mouse):
                before_playing = True
                after_playing = False
                gameplay = False
                Welcome_text_x = 150
                Welcome_text_y = 50
                Play_text_x = 650
                Play_text_y = 250
                Settings_text_x = 580
                Settings_text_y = 400
                Quit_text_x = 645
                Quit_text_y = 550
                Language_text_x = 100
                Language_text_y = 700
                Choose_game_speed_text_x = 10000
                Choose_game_speed_text_y = 10000
                game_speed_text1_x = 10000
                game_speed_text1_y = 10000
                game_speed_text2_x = 10000
                game_speed_text2_y = 10000
                game_speed_text3_x = 10000
                game_speed_text3_y = 10000
                game_speed_text4_x = 10000
                game_speed_text4_y = 10000
                Back_text_x = 10000
                Back_text_y = 10000
        if event.type == bullet_timer1:
            bullet_list_in_game1.append(bullet1.get_rect(topleft=(player1_x + 15, player1_y - 27)))
        if event.type == bullet_timer2:
            bullet_list_in_game2.append(bullet2.get_rect(topleft=(player2_x + 15, player2_y + 63)))
    
    pygame.display.update()
