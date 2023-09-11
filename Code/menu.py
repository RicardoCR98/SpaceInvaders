import pygame

class MainMenu:
    def __init__(self, screen_width, screen_height, score_manager):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 36)
        self.options = ["Iniciar Juego", "Ver Puntajes", "Salir"]
        self.selected_option = 0
        self.score_manager = score_manager

    def draw(self, screen):
        title_text = self.font.render("Space invaders", True, (255, 255, 255))
        screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))

        option_spacing = 50  # Espacio vertical entre opciones

        # Posición vertical inicial
        start_y = self.screen_height // 2 - (len(self.options) * option_spacing) // 2

        # Posición horizontal de las opciones
        start_x_left = self.screen_width // 4  # Izquierda
        start_x_right = self.screen_width * 3 // 4  # Derecha

        start_y_up = self.screen_height*1.5 // 4  # Arriba

        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))

            y = start_y + i * option_spacing

            if i == 0:
                x = start_x_left - text.get_width() // 2
            elif i == 2:
                #x = start_x_right - text.get_width() // 2
                y = start_y_up - text.get_height() //4  # Puedes ajustar la cantidad de desplazamiento aquí
                x = start_x_right - text.get_width() // 2
            else:
                x = self.screen_width // 2 - text.get_width() // 2

            if self.selected_option == i:
                pygame.draw.rect(screen, (255, 255, 255), (x - 10, y - 5, text.get_width() + 20, text.get_height() + 10), 3)
            screen.blit(text, (x, y))
            
        if self.selected_option == 1:
            top_scores = self.score_manager.get_top_scores()
            y_ver_puntajes = start_y + len(self.options) * 35  # Alinea en el centro verticalmente debajo de las opciones
            for score in top_scores:
                score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
                screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, y_ver_puntajes))
                y_ver_puntajes += option_spacing

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








