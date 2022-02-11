import pygame


# Just placed these functions in the class for scaffolding. 
class Engine:
    running = False
    width = 1024
    height = 768
    visible_statistics = False

    def __init__(self, title, scene, ):
        self.title = title
        self.scene = scene

    def toggle_statistics(self):
        self.visible_statistics = True
    
    def show_statistics():
        pass
    
    def init_pygame():
        pass

    def run():
        pass
    
    def stop():
        pass

    def end():
        pass



class Scene:
    updateables = []
    drawables: pygame.sprite.LayeredDirty
    fps = 30
    
    def __init__(self, name):
        self.name = name
    
    def set_fps(self, fps):
        self.fps = fps

