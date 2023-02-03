import pygame

INIT_VIEW_PORT_SIZE = (700,500)
SCALE = 1.7 # keep scale to 1.7 for now. later we might have config/option for it

class Display:

    # it is good practice to separate the screen and view port
    screen = None
    view_port = None 

    def setup():  
    
        W,H = INIT_VIEW_PORT_SIZE

        Display.screen = pygame.display.set_mode(
            size = ( W*SCALE, H*SCALE ), 
            flags = pygame.RESIZABLE, 
            depth = 32
        )
        pygame.display.set_caption("Survival")
        Display.view_port = pygame.Surface( ( W, H ) )


    def sync_view_port_to_screen():

        # If scale = 1 this is somewhat unnecessary. To save performance make
        # another solution for just scale = 1 perhaps?

        s = Display.screen
        vp = Display.view_port

        s.blit( pygame.transform.scale( vp, s.get_size() ), (0,0) )


    def on_resize(size):
        W,H = size
        Display.view_port = pygame.Surface( ( W/SCALE, H/SCALE ) )


