import pygame
import random
from food import Food


class Snake:

    def __init__(self, *args, **kwargs):
        self.game_over = False
        self.display_width = 800
        self.display_height = 600
        self.snake_length = 1
        self.score = 0
        self.prev_key = None
        self.color = {
            'lime': (0, 255, 0),
            'white': (255, 255, 255),
            'gray': (128, 128, 128)
        }

        # Screen dimensions
        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height))
        self.clock = pygame.time.Clock()

        # Snake starts at the center of the display
        self.x_pos = self.display_width / 2
        self.y_pos = self.display_height / 2
        self.snake = [
            (self.x_pos, self.y_pos)
        ]

        # Snake will not move until an arrow key is pressed
        self.x_speed = 0
        self.y_speed = 0

        self.snake_food = Food(display_width=self.display_width, display_height=self.display_height)

    def start(self):
        pygame.display.update()
        self.update_caption()
        self.play_game()

    def play_game(self):
        self.snake_food.generate_food()
        while (self.snake_food.x_pos, self.snake_food.y_pos) in self.snake:
            self.snake_food.generate_food()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.move_down(event.key)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.move_left(event.key)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.move_up(event.key)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.move_right(event.key)
            self.display.fill(self.color['gray'])
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed
            self.snake.append((self.x_pos, self.y_pos))

            if self.x_pos == self.snake_food.x_pos and self.y_pos == self.snake_food.y_pos:
                self.snake_food.generate_food()
                self.snake_length += 1
                self.score += 10
                self.update_caption()

            if len(self.snake) > self.snake_length:
                del self.snake[0]

            if self.x_pos > self.display_width or self.x_pos < 0 or self.y_pos > self.display_height or self.y_pos < 0:
                self.game_over = True
                self.reset_game()

            pygame.draw.rect(self.display, self.color['white'], [
                             self.snake_food.x_pos, self.snake_food.y_pos, 10, 10])
            for x, y in self.snake:
                pygame.draw.rect(
                    self.display, self.color['lime'], [x, y, 10, 10])
            pygame.display.update()

            # Runs game at 30 FPS
            self.clock.tick(30)

    def move_right(self, event_key):
        if self.snake_length == 1 or self.prev_key not in (pygame.K_LEFT, pygame.K_a):
            self.x_speed = 10
            self.y_speed = 0
            self.prev_key = event_key

    def move_left(self, event_key):
        if self.snake_length == 1 or self.prev_key not in (pygame.K_RIGHT, pygame.K_d):
            self.x_speed = -10
            self.y_speed = 0
            self.prev_key = event_key

    def move_down(self, event_key):
        if self.snake_length == 1 or self.prev_key not in (pygame.K_UP, pygame.K_w):
            self.x_speed = 0
            self.y_speed = 10
            self.prev_key = event_key

    def move_up(self, event_key):
        if self.snake_length == 1 or self.prev_key not in (pygame.K_DOWN, pygame.K_s):
            self.x_speed = 0
            self.y_speed = -10
            self.prev_key = event_key

    def reset_game(self):
        self.game_over = False
        self.snake.clear()
        self.snake_length = 1
        self.x_pos = self.display_width / 2
        self.y_pos = self.display_height / 2
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.snake_food.generate_food()
        self.update_caption()

    def update_caption(self):
        pygame.display.set_caption(f'Snake Block Eater | Score: {self.score}')


snake = Snake()
snake.start()
