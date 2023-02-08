
import pygame
import random



class Rain:


    drops = [ [0,0] for _ in range(120) ]

    def draw( at_surface ):
        from frame_counter import FrameCounter

        f = FrameCounter.get_frame()
        



        s = pygame.Surface( at_surface.get_size(), pygame.SRCALPHA  )



        for drop in Rain.drops:
            drop[1] += 12
            if drop[1] > 400:
                drop[1] = -40- random.randrange(400)
                drop[0] = random.randrange( at_surface.get_size()[0]-1 )

        for e, drop in enumerate(Rain.drops):
            x,y = drop
            pygame.draw.rect( s, (0x77,0x77,0x77,e+20), (x-y//20,y,1,20) )

        at_surface.blit(s,(0,0))


