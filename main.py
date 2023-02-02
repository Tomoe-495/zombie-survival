import pygame
import sys
from player import Player
import tilemap


W, H = 600, 400
FPS = 60
SCALE = 2

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((W*SCALE, H*SCALE), 0, 32)
canvas = pygame.Surface( ( W, H ) )
pygame.display.set_caption("Survival")


def main():
    run = True

    player = Player()
    tile = tilemap.Tiledmap()

    def draw(win):
        win.fill((180, 0, 60))

        player.draw(win, tile.scroll)
        tile.draw(win)

        pygame.display.update()


    while run:
        clock.tick(FPS)

        draw(canvas)
        win.blit( pygame.transform.scale( canvas, win.get_size() ), (0,0) )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
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

        tile.camera(player)


    sys.exit()

if __name__ == "__main__":
    main()
