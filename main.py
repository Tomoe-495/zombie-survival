import pygame
import sys
from player import Player
import tilemap
from display import Display
from camera import Camera

W, H = 1400, 800
FPS = 60

pygame.init()
clock = pygame.time.Clock()

Display.setup()


def scene_position_to_view_port_position( scene_position ):

    camera = Camera.get_camera()

    return [
        Display.view_port.get_rect().center[i] + scene_position[i] - camera[i]
        for i in range(2)
    ]


def main():
    run = True

    tile = tilemap.Tiledmap()
    player = Player()

    Camera.follow( player )

    def draw(win):
        win.fill((144, 244, 200))

        # player will now be drawn with the tiles, cuz of layerings
        tile.draw(player, win)



    while run:
        clock.tick(FPS)

        draw( Display.view_port )
        Display.sync_view_port_to_screen()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.VIDEORESIZE:
                Display.on_resize( event.size )

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

        Camera.step()
        #tile.camera(player)


    sys.exit()

if __name__ == "__main__":
    main()
