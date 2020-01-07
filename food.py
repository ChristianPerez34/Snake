import random

class Food:

    def __init__(self, *args, **kwargs):
        self.display_width = kwargs.pop('display_width')
        self.display_height = kwargs.pop('display_height')
        self.x_pos = 0
        self.y_pos = 0

    def generate_food(self):
        self.x_pos = random.randrange(0, self.display_width, 10)
        self.y_pos = random.randrange(0, self.display_height, 10)