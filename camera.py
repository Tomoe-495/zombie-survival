class Camera:

    follow = None
    
    def follow( follow ):
        Camera.follow = follow


    def get_camera():
        return Camera.follow.rect.center


