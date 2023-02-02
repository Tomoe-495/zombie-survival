import pygame
import sys
from player import Player
import tilemap


W, H = 1000, 400
FPS = 60

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption("Survival")


def main():
    run = True

    player = Player()
    tile = tilemap.Tiledmap()

    def draw(win):
        win.fill((180, 0, 60))

        player.draw(win)
        tile.draw(win)

        pygame.display.update()


    while run:
        clock.tick(FPS)

        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left = True
                if event.key == pygame.K_RIGHT:
                    player.right = True
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.left = False
                if event.key == pygame.K_RIGHT:
                    player.right = False
        
        movement = [0, 0]

        player.update(movement)
        player.platformer(movement, tile.tiles)


if __name__ == "__main__":
    main()
