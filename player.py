import pygame
from framework import move

"""
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pygame.Surface((20, 30))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.right = False
        self.left = False
        self.speed = 0
        self.max_speed = 2
        self.vel = 0
        self.acc = 0.5
        self.ACC = 0.4
        self.jump_count = 0
        self.jump_limit = 9
        self.jump_power = -4
    
    def draw(self, win, scroll):
        from main import scene_position_to_view_port_position
        projected_position = scene_position_to_view_port_position( self.rect[:2] )  
        win.blit(
            self.image, 
            projected_position
        )

    def jump(self):
        if self.jump_count < self.jump_limit:
            self.vel = self.jump_power
            self.jump_count += 1    
    
    def update(self, movement):
        if self.right:
            if self.speed < self.max_speed:
                self.speed += self.acc
        elif self.left:
            if self.speed > -self.max_speed:
                self.speed -= self.acc
        else:
            if self.speed > 0:
                self.speed -= self.acc
            elif self.speed < 0:
                self.speed += self.acc
        
        movement[0] += self.speed

        #   gravity
        movement[1] += self.vel
        self.vel += self.ACC

    def platformer(self, movement, tiles):
        self.rect, collisions = move(self.rect, movement, tiles)

        if collisions["bottom"]:
            self.vel = 0
            self.jump_count = 0
"""

def offset2d( a, b ):
    return (a[0] + b[0]), (a[1] + b[1])

class Player:

    def __init__( self ):
        from tilemap import Tiledmap
        self.x_position = Tiledmap.current.size*5
        self.y_tile = 11 
        self.left = None
        self.right = None
    
    def jump( self ):
        pass

    def get_stand_on_cell_value( self, x_position = None, y_tile_offset = 0 ):
        from tilemap import Tiledmap
        cp = self.get_stand_on_cell_position( x_position, y_tile_offset)
        return Tiledmap.current.cells.get( cp, 0 )

    def get_stand_on_cell_position( self, x_position = None, y_tile_offset = 0 ):
        from tilemap import Tiledmap

        if x_position is None:
            x_position = self.x_position

        return (
            x_position // Tiledmap.current.size,
            self.y_tile + y_tile_offset
        )

    def get_position( self ):
        from tilemap import Tiledmap
        TILE_SIZE = Tiledmap.current.size

        cell = self.get_stand_on_cell_value()

        if cell == 1:
            return (
                self.x_position,
                self.y_tile*TILE_SIZE,
            )
        if cell == 2:
            return (
                self.x_position,
                self.y_tile*TILE_SIZE + TILE_SIZE - self.x_position % TILE_SIZE,
            )
        if cell == 3:
            return (
                self.x_position,
                self.y_tile*TILE_SIZE + self.x_position % TILE_SIZE,
            )


    def update( self, movement ):
        from tilemap import Tiledmap

        new_x_position = self.x_position


        if self.left:
            new_x_position = self.x_position - 1
            direction = 'left'
        elif self.right:
            new_x_position = self.x_position + 1
            direction = 'right'
        else:
            return

        new_cell = self.get_stand_on_cell_value( x_position = new_x_position )
        new_cell_top = self.get_stand_on_cell_value( x_position = new_x_position, y_tile_offset= -1 )
        new_cell_bottom = self.get_stand_on_cell_value( x_position = new_x_position, y_tile_offset= 1 )


        if direction == 'right' and new_cell_top == 2:
            self.y_tile -= 1
            self.x_position = new_x_position
            return

        if direction == 'left' and new_cell_top == 3:

            self.x_position = new_x_position
            self.y_tile -= 1
            return



        if new_cell_top == 1:
            return


        if new_cell in (1,2,3):
            self.x_position = new_x_position
            return

        if direction == 'left' and new_cell_bottom in (1,2):
            self.x_position = new_x_position
            self.y_tile += 1
            return

        if direction == 'right' and new_cell_bottom in (1,3):
            self.x_position = new_x_position
            self.y_tile += 1
            return

        #if v == 1:
        #    self.x_position = new_x_position

    def draw( self, draw_at):
        from main import scene_position_to_view_port_position
        pp = projected_position = scene_position_to_view_port_position( self.get_position() )  
 

        #r = tuple(map(round,projected_position))
        #print(r)
        pygame.draw.rect( draw_at, 0xFF0000, (*offset2d( pp, (-10,-20)),20,20) )

    def platformer(self, movement, tiles):
        pass

