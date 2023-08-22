import pygame
import  sys
from game import Game



if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game(screen, screen_width, screen_height)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)
    in_main_menu = True
    
    while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if in_main_menu:
            action = main_menu.handle_event(event)
            if action == "start_game":
                in_main_menu = False
            elif action == "quit":
                pygame.quit()
                sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.paused = not game.paused 
            if not game.paused:
                
                if event.type == ALIENLASER:
                   game.alien_shoot()
    screen.fill((30, 30, 30))

    if in_main_menu:
        main_menu.draw(screen)
    else:
        if game.paused:
           pause_message = game.font.render("PAUSA", True, (255, 255, 255))
           screen.blit(pause_message, (screen_width // 2 - pause_message.get_width() // 2, screen_height // 2 - pause_message.get_height() // 2))
        else:
          game.run()

    pygame.display.flip()
    clock.tick(60)



 
