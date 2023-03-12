import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 255, 255), player)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(player)
    pygame.quit()

if __name__ == "__main__":
    main()
