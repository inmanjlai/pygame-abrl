import pygame

class StatusBar:
    def __init__(self, screen, x, y, character):
        self.screen = screen
        self.x = x
        self.y = y
        self.character = character

    def draw(self, hp):
        self.hp = hp
        hp_ratio = self.character.hp / self.character.max_hp
        # attack_ratio = self.character.attack_energy / 100
        # defense_ratio = self.character.defense_energy / 100
        # HEALTH
        pygame.draw.rect(self.screen, (255, 100, 100), pygame.Rect(self.x, self.y, 150, 20))
        pygame.draw.rect(self.screen, (100, 255, 100), pygame.Rect(self.x, self.y, 150 * hp_ratio, 20))
        # ATTACK ENERGY
        # pygame.draw.rect(self.screen, (155, 100, 155), pygame.Rect(self.x, self.y+20, 150, 20))
        # pygame.draw.rect(self.screen, (255, 100, 100), pygame.Rect(self.x, self.y+20, 150 * attack_ratio, 20))
        # #DEFENSE ENERGY
        # pygame.draw.rect(self.screen, (155, 100, 155), pygame.Rect(self.x, self.y+40, 150, 20))
        # pygame.draw.rect(self.screen, (100, 100, 255), pygame.Rect(self.x, self.y+40, 150 * defense_ratio, 20))
