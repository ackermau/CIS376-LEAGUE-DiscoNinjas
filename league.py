import pygame
from pygame.locals import (
    KEYDOWN,
    K_SPACE,
)

# Just placed these functions in the class for scaffolding.
class Engine:
    running = False
    width = 800
    height = 800
    visible_statistics = False
    delta_time = 0
    events = None

# Sets the title and the scene for the engine
    def __init__(self, title, scene):
        self.title = title
        self.scene = scene


    def toggle_statistics(self):
        self.visible_statistics = True

    def show_statistics():
        pass

    def init_pygame(self):
        pygame.init()
        

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
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            current = pygame.time.get_ticks()
            last = current
            delta = current - last

            # This gotta be bad?
            # Resets background to move an object without a copy of it
            screen.fill(background_color)

            # Call updataeables
            for obj in self.scene.updateables:
                obj.update()

            # Call drawables
            for obj in self.scene.drawables:
                obj.draw(screen)

            #changes the display to the second buffer?
            pygame.display.flip()

            # Busy wait until our delta time is equal to our target frame time in ms.
            while delta < targetFrameTime:
                current = pygame.time.get_ticks()
                delta = current - last
                self.delta_time = delta / 1000

            # If frames get too high the game will quit
            if delta > 1000:
                pygame.quit()



    def stop(self):
        self.running = False

    def end():
        pass



class Scene:
    #Initializes the frames, draw gameobjects array, and the updateables array
    
    updateables = []
    drawables = []
    collideables = []
    fps = 30

    #Sets the Scene name

    def __init__(self, name):
        self.name = name

    #Sets the Fps

    def set_fps(self, fps):
        self.fps = fps



class GameObject:
    def __init__(self):
        self.x = 50
        self.y = 50
    

class UGameObject(GameObject):
    def update(self):
        pass

#Draw Class implamented by gameObjects

class DGameObject(GameObject):
    def draw(self, screen):
        screen.blit(self.image, self.rect)

#Draw Update Class implamented by gameObjects

class DUGameObject(UGameObject):
    # Implements just draw. Inherits update from UGameObject.
    def draw(self, screen):
        screen.blit(self.image, self.rect)
