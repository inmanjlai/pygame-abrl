import pygame

class Character:
    def __init__(self, screen, x, y, name, max_hp, attack_gen, defense_gen):
        self.screen = screen
        self.x = x
        self.y = y
        self.name = name
        img = pygame.image.load(f'./assets/{name}.png')
        self.image = pygame.transform.smoothscale(img, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.alive = True

        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = 1
        self.gold = 0
        self.attack_energy = 0
        self.defense_energy = 0
        self.attack_gen = attack_gen
        self.defense_gen = defense_gen

    def draw(self):
        self.screen.blit(self.image, (self.rect))

    def attack(self, target):
        if target.hp <= 0:
            target.alive = False

class Monk(Character):
    def attack(self, target):
        target.hp -= 1 + self.strength
        return super().attack(target)

class Rogue(Character):
    def attack(self, target):
        target.hp -= 5 + self.strength
        return super().attack(target)
