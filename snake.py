import pygame

game_over = False
display = pygame.display.set_mode((400, 300))
pygame.display.update()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        print(event)   #prints out all the actions that take place on the screen
# pygame.quit()
# quit()