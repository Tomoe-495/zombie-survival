import pygame

INIT_SCREEN_SIZE  = (1400,800)
SCALE = 4

class Display:

    # it is good practice to separate the screen and view port
    screen = None
    view_port = None 

    def setup():  
    

        Display.screen = pygame.display.set_mode(
            size = INIT_SCREEN_SIZE, 
            flags = pygame.RESIZABLE,
            depth = 32
        )

        if Display.screen.get_size() != INIT_SCREEN_SIZE:
            print("Warning: requested screen size was {0}, but it ended up being {1}".format( INIT_SCREEN_SIZE, Display.screen.get_size() ))
        
        pygame.display.set_caption("Survival")
        
        Display.refresh_view_port_size()


    def refresh_view_port_size():
        Display.view_port = pygame.Surface( Display.get_the_view_port_size_based_on_screen_size() )


    def get_the_view_port_size_based_on_screen_size():
        return [ Display.screen.get_size()[i] / SCALE for i in range(2) ]


    def sync_view_port_to_screen():

        # If scale = 1 this is somewhat unnecessary. To save performance make
        # another solution for just scale = 1 perhaps?

        s = Display.screen
        vp = Display.view_port

        s.blit( pygame.transform.scale( vp, s.get_size() ), (0,0) )


    def on_resize(size):
        Display.refresh_view_port_size()


