import asyncio
import pygame
import sys
from player import Player
import tilemap
from display import Display
from camera import Camera

FPS = 60


def scene_position_to_view_port_position( scene_position ):


    camera = Camera.get_camera()

    return [
        Display.view_port.get_rect().center[i] + scene_position[i] - camera[i]
        for i in range(2)
    ]




async def main():
    run = True

    pygame.font.init()

    font = pygame.font.Font(None,32)

    while run:

        # --- grab events
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
        # ---        

        # --- game logic        
        movement = [0, 0]

        player.update(movement)
        player.platformer(movement, tile.tiles)

        Camera.step()
        # ---

        # --- draw and sync logic
        Display.view_port.fill((100, 244, 200))
        tile.draw(player, Display.view_port  )
        Display.sync_view_port_to_screen()

        Display.screen.blit( 
            font.render( str(round(clock.get_fps())), (0,0,0), True ),
            (0,0),
        )
        
        clock.tick(FPS)
        pygame.display.update()

        await asyncio.sleep(0)
        # ---

    sys.exit()



if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()

    Display.setup()



    tile = tilemap.Tiledmap()
    player = Player()

    Camera.follow( player )



    asyncio.run( main() )





