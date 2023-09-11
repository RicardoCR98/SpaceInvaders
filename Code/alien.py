import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, enemies, x, y):
        super().__init__()
        file_path = 'Graphics/' + enemies + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        #Puntuacion de Aliens
        if enemies == 'yellow':
            self.score_value = 15  # Puntuación para alienígenas amarillos
        elif enemies == 'green':
            self.score_value = 10  # Puntuación para alienígenas verdes
        elif enemies == 'red':
            self.score_value = 5  # Puntuación para alienígenas rojos
        elif enemies == 'extra':
            self.score_value = 20  # Puntuación para otros alienígenas

    def down_a_row(self, distance):
        self.rect.y += distance

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load('Graphics/extra.png').convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x, 80))

    def update(self):
        self.rect.x += self.speed