import pygame

STEP_FACTOR = 0.1 # adjust this to change smooth camera

class Camera:

    _follow = None
    _camera_position = None

    def follow( follow ):
        Camera._follow = follow
        Camera._camera_position = Camera.get_target_position().copy()


    def step():
        Camera._camera_position = Camera._camera_position.lerp( Camera.get_target_position(), STEP_FACTOR )


    def get_target_position():
        return pygame.math.Vector2( Camera._follow.rect.center )


    def get_camera():
        return Camera._camera_position.copy()
