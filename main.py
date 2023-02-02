import pygame
import sys
from drawing import draw

W, H = 1000, 400
FPS = 60

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption("Survival")


def main():
    run = True

    while run:
        clock.tick(FPS)

        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()


if __name__ == "__main__":
    main()
