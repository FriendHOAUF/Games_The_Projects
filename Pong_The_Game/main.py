import pygame

pygame.init()

# Game windown
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pygame Test")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
