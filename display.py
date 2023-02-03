import pygame

W, H = 1400, 800
w, h = W/4, H/4

class Display:

    # it is good practice to separate the screen and view port
    screen = None
    view_port = None 

    def setup():  
    

        Display.screen = pygame.display.set_mode(
            size = ( W, H ), 
            flags = pygame.RESIZABLE,
            depth = 32
        )
        pygame.display.set_caption("Survival")
        Display.view_port = pygame.Surface( ( w, h ) )


    def sync_view_port_to_screen():

        # If scale = 1 this is somewhat unnecessary. To save performance make
        # another solution for just scale = 1 perhaps?

        s = Display.screen
        vp = Display.view_port

        s.blit( pygame.transform.scale( vp, s.get_size() ), (0,0) )


    def on_resize(size):
        W,H = size
        Display.view_port = pygame.Surface( ( w, h ) )


