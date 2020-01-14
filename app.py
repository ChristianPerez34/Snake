import pygame

class App:

    def __init__(self, *args, **kwargs):
        self.display_width = 800
        self.display_height = 600
        self.score = 0

        self.display = None
        self.clock = None
        self.prev_key = None

        self.game_over = False
        
        self.color = {
            'lime': (0, 255, 0),
            'white': (255, 255, 255),
            'gray': (128, 128, 128)
        }

    def start(self):
        self.create_display()
        self.update_caption()

    def create_display(self):
        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height))
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def update_caption(self):
        pygame.display.set_caption(f'Snake Block Eater | Score: {self.score}')
        