import pygame
import sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        # configuration de la nave
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # configuration del obstacle
        self.shape = obstacle.shape1
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_position = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_position, x_start=screen_width / 15, y_start=480)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.alien_laser = pygame.sprite.Group()
        self.alien_direction = 1

        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40,80)

        #Player
        self.lives = 3
        self.game_over = False


    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6, screen_height)
            self.alien_laser.add(laser_sprite)

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right','left']),screen_width))
            self.extra_spawn_time = randint(400,800)

    def collision_checks(self):
        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collisions
                #if pygame.sprite.spritecollide(laser, self.aliens, True):
                 #   laser.kill()
                  #puntuacion al destruir los aliens
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                for alien in aliens_hit:
                    laser.kill()
                    self.player.sprite.score += alien.score_value

                # extra collision
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()

                

        # alien lasers
        if self.alien_laser:
            for laser in self.alien_laser:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    print('EL JUGADOR A MUERTO')
                    #vidas del jugador
                    self.lives -= 1
                    if self.lives <= 0:
                        self.lives = 0
                        self.game_over = True

        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()

                    #self.game_over = True  #Game over

                    sys.exit()
                    


    def run(self):
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_position_checker()
        self.alien_laser.update()
        self.extra_alien_timer()
        self.extra.update()
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_laser.draw(screen)
        self.extra.draw(screen)
        # update all sprite groups
        # draw all sprite 

        
         #vidas
        font = pygame.font.Font(None, 30)
        lives_text = font.render(f'Lives: {self.lives}', True, (255, 255, 255))
        screen.blit(lives_text, (10, 20))  # Ajusta la posición según tu preferencia

        #pygame.display.flip()
        #clock.tick(60)

        #puntuacion
        font = pygame.font.Font(None, 30)
        score_text = font.render(f'Score: {self.player.sprite.score}', True, (255, 255, 255))
        screen.blit(score_text, (110, 20))  # Ajusta la posición según tu preferencia

        #Game over
        if self.game_over:
            font = pygame.font.Font(None, 60)
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (screen_width // 2 - 120, screen_height // 2))
            pygame.display.flip()
            return  # Detener la actualización si el juego ha terminado
        

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
        screen.fill((30, 30, 30))
        game.run()
        pygame.display.flip()
        clock.tick(60)
