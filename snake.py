import pygame

game_over = False
x_pos = 300
y_pos = 300
x_speed = 0
y_speed = 0

color = {
    'lime': (0, 255, 0),
    'white': (255, 255, 255)
}

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.update()
pygame.display.set_caption('Lifeline Snake')

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                x_speed = 0
                y_speed = 10
            elif event.key == pygame.K_LEFT:
                x_speed = -10
                y_speed = 0
            elif event.key == pygame.K_UP:
                x_speed = 0
                y_speed = -10
            elif event.key == pygame.K_RIGHT:
                x_speed = 10
                y_speed = 0
    x_pos += x_speed
    y_pos += y_speed
    display.fill(color['white'])
    pygame.draw.rect(display, color['lime'], [x_pos, y_pos, 10, 10])
    pygame.display.update()
    clock.tick(25)