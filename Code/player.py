import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load('Graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        #Variables para el disparo
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 1000
        self.lasers = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('Audio/laser.wav')
        self.laser_sound.set_volume(0.05)

        #puntuacion
        self.score = 0

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        #Implementar mecánica de disparo
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        """Función de recarga, se vizualiza la resta entre el tiempo actual y el tiempo desde que se
        disparó el ultimo proyectil, si ese tiempo es mayor al cooldawn entonces el boleano se cambia
        a verdadero para volver a tener la posibilidad de dispara."""
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time > self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    # Añadir mecánica de disparo
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,-6,self.rect.bottom))
        self.laser_sound.play()
    def update(self):

        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()