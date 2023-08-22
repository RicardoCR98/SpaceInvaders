import pygame
class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 36)
        self.options = ["Iniciar Juego", "Ver Puntajes", "Salir"]
        self.selected_option = 0

    def draw(self, screen):
        title_text = self.font.render("Juego Espacial", True, (255, 255, 255))
        screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            x = self.screen_width // 2 - text.get_width() // 2
            y = 200 + i * 50
            if self.selected_option == i:
                pygame.draw.rect(screen, (255, 255, 255), (x - 10, y - 5, text.get_width() + 20, text.get_height() + 10), 3)
            screen.blit(text, (x, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    return "start_game"
                elif self.selected_option == 1:
                    return "view_scores"
                elif self.selected_option == 2:
                    return "quit"
        return None








