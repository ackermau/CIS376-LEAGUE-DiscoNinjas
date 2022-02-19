import pygame


# Just placed these functions in the class for scaffolding.
class Engine:
    running = False
    width = 1024
    height = 768
    visible_statistics = False
    delta_time = 0

    def __init__(self, title, scene):
        self.title = title
        self.scene = scene

    def toggle_statistics(self):
        self.visible_statistics = True

    def show_statistics():
        pass

    def init_pygame():
        pass

    def run(self):

        background_color = (234, 212, 252)


        # Define the dimensions of
        # screen object(width,height)
        screen = pygame.display.set_mode((self.width, self.height))

        # Set the caption of the screen
        pygame.display.set_caption(self.title)

        # Fill the background colour to the screen
        screen.fill(background_color)


        self.running = True

        targetFrameTime = 1000/self.scene.fps

        while self.running:
            pygame.init()
            current = pygame.time.get_ticks()
            last = current
            delta = current - last

            # Call updataeables
            for obj in self.scene.updateables:
                obj.update()

            # Call drawables
            # for obj in self.scene.drawables:
            #     obj.update()

            pygame.display.flip()

            # Busy wait until our delta time is equal to our target frame time in ms.
            while delta < targetFrameTime:
                current = pygame.time.get_ticks()
                delta = current - last
                self.delta_time = delta / 1000



    def stop(self):
        self.running = False

    def end():
        pass



class Scene:
    updateables = []
    drawables: pygame.sprite.LayeredDirty = []
    fps = 30
    
    def __init__(self, name):
        self.name = name
    
    def set_fps(self, fps):
        self.fps = fps



class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class UGameObject(GameObject):
    # Implements just update
    pass


class DGameObject(GameObject):
    # Implements just draw
    pass


class DUGameObject(UGameObject):
    # Implements just draw. Inherits update from UGameObject.
    pass