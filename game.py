import pygame
from character import Rogue, Monk
from statusbar import StatusBar

pygame.init()

WIDTH, HEIGHT = 800, 450
font = pygame.font.SysFont('Arial', 26)
fps = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(text, font, color, x, y):
     img = font.render(text, True, color)
     screen.blit(img, (x, y))

def draw_bg():
    screen.fill((75, 75, 75))

screen_center_height = (HEIGHT / 2 - 20)

player = Rogue(screen, 150, screen_center_height, 'rogue', 85, 25, 35)
player_healthbar = StatusBar(screen, 85, HEIGHT - 80, player)

enemy = Monk(screen, 600, screen_center_height, 'monk_f', 100, 15, 25)
enemy_healthbar = StatusBar(screen, 550, HEIGHT - 80, enemy)


current_turn = { "count": 1, "fighter": player }

def new_enemy():
    enemy = Monk(screen, 600, screen_center_height, 'monk_f', 100, 15, 25)
    enemy_healthbar = StatusBar(screen, 550, HEIGHT - 80, enemy)
    return [enemy, enemy_healthbar]

def fight_end():
    active = True
    while active:
        screen.fill((50, 50, 50))

        draw_text('Press ESC to continue', font, (255, 255, 255), 250, screen_center_height)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False
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

def reset_battle():
    enemy.hp = enemy.max_hp
    enemy.alive = True

running = True
while running:

    clock.tick(fps)

    draw_bg()

    player.draw()
    player_healthbar.draw(player.hp)

    enemy.draw()
    enemy_healthbar.draw(enemy.hp)

    new_battle = fight()

    if new_battle != None:
        enemy = new_battle[0]
        enemy_healthbar = new_battle[1]
        reset_battle()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
