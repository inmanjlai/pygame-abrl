import pygame, sys
from character import Rogue, Monk
from statusbar import StatusBar

pygame.init()

# CONFIG

WIDTH, HEIGHT = 800, 450
font = pygame.font.SysFont('Arial', 26)
fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(text, font, color, x, y):
     img = font.render(text, True, color)
     screen.blit(img, (x, y))

def draw_bg():
    screen.fill((75, 75, 75))

screen_center_height = (HEIGHT / 2 - 20)

player = Rogue(screen, 150, screen_center_height, 'rogue', 100, 25, 35)
player_healthbar = StatusBar(screen, 85, HEIGHT - 80, player)

enemy = Monk(screen, 600, screen_center_height, 'monk_f', 100, 15, 25)
enemy_healthbar = StatusBar(screen, 550, HEIGHT - 80, enemy)

# BATTLE METHODS

battle_count = 1
current_turn = { "count": 1, "fighter": player }

def new_enemy():
    enemy = Monk(screen, 600, screen_center_height, 'monk_f', 100, 15, 25)
    enemy_healthbar = StatusBar(screen, 550, HEIGHT - 80, enemy)
    return [enemy, enemy_healthbar]

def new_player():
    player = Rogue(screen, 150, screen_center_height, 'rogue', 100, 25, 35)
    player_healthbar = StatusBar(screen, 85, HEIGHT - 80, player)
    return [player, player_healthbar]

def choice():
    screen.fill((50, 50, 50))
    draw_text('Press 1 for gold', font, (255, 255, 255), 250, screen_center_height)
    draw_text('Press 2 for power', font, (255, 255, 255), 250, screen_center_height + 30)
    draw_text('Press 3 for health', font, (255, 255, 255), 250, screen_center_height + 60)

def fight_end():
    active = True
    while active:
        choice()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    active = False
                    player.gold += 10
                    return new_enemy()
                if event.key == pygame.K_2:
                    active = False
                    player.strength += 1
                    return new_enemy()
                if event.key == pygame.K_3:
                    active = False
                    player.hp += 50
                    player.max_hp += 5
                    return new_enemy()
                
        pygame.display.update()


def end_turn():
    win = False
    if enemy.alive == False:
        win = True

    current_turn['count'] += 1
    if current_turn['fighter'] == player:
        current_turn['fighter'] = enemy
    else:
        current_turn['fighter'] = player

    if win:
        return fight_end()

def fight():
    target = enemy
    if current_turn['fighter'] == player:
        target = enemy
    else:
        target = player

    if current_turn['fighter'].alive == True:
        current_turn['fighter'].attack(target)
        return end_turn()
    else:
        return end_turn()

def next_battle():
    global battle_count 
    battle_count += 1
    enemy.max_hp = enemy.max_hp + 5 * battle_count
    enemy.hp = enemy.max_hp
    enemy.alive = True

def new_game():
    global battle_count
    battle_count = 1
    player.hp = player.max_hp
    player.alive = True
    enemy.hp = enemy.max_hp
    enemy.alive = True
    return [new_player(), new_enemy()]

def lose():
    active = True
    while active:
        screen.fill((50, 50, 50))

        draw_text('You died...', font, (255, 255, 255), 250, screen_center_height)
        draw_text('Press SPACE to restart', font, (255, 255, 255), 250, screen_center_height + 30)
        draw_text('Press ESC to quit', font, (255, 255, 255), 250, screen_center_height + 60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = False
                    return new_game()
                if event.key == pygame.K_ESCAPE:
                    active = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# GAME LOOP

running = True
while running:

    clock.tick(fps)

    draw_bg()

    draw_text(f'Gold: {player.gold}', font, (255, 255, 255), 25, 25)

    player.draw()
    player_healthbar.draw(player.hp)

    enemy.draw()
    enemy_healthbar.draw(enemy.hp)

    new_battle = fight()

    if new_battle != None:
        enemy = new_battle[0]
        enemy_healthbar = new_battle[1]
        next_battle()


    if player.alive == False:
        start_new_game = lose()

        if new_game != None:
            player = start_new_game[0][0]
            player_healthbar = start_new_game[0][1]
            enemy = start_new_game[1][0]
            enemy_healthbar = start_new_game[1][1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
