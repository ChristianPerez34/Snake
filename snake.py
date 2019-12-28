import pygame


class Snake:

    def __init__(self, *args, **kwargs):
        self.game_over = False
        self.display_width = 800
        self.display_height = 600
        self.color = {
            'lime': (0, 255, 0),
            'white': (255, 255, 255),
            'gray': (128, 128, 128)
        }
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()

        # Snake starts at the center of the display
        self.x_pos = self.display_width / 2
        self.y_pos = self.display_height / 2

        # Snake will not move until an arrow key is pressed
        self.x_speed = 0
        self.y_speed = 0
    
    def start(self):
        pygame.display.update()
        pygame.display.set_caption('Snake Block Eater')
        self.play_game()
    
    def play_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.x_speed = 0
                        self.y_speed = 10
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.x_speed = -10
                        self.y_speed = 0
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.x_speed = 0
                        self.y_speed = -10
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.x_speed = 10
                        self.y_speed = 0
            self.display.fill(self.color['gray'])
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed
            if self.x_pos > self.display_width or self.x_pos < 0 or self.y_pos > self.display_height or self.y_pos < 0:
                self.game_over = True
                self.reset_game()
            pygame.draw.rect(self.display, self.color['lime'], [self.x_pos, self.y_pos, 10, 10])
            pygame.display.update()

            # Runs game at 30 FPS
            self.clock.tick(30)

    def reset_game(self):
        self.game_over = False
        self.x_pos = self.display_width / 2
        self.y_pos = self.display_height / 2
        self.x_speed = 0
        self.y_speed = 0

snake = Snake()
snake.start()
    
