import pygame
import random

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn 
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
        

   
class Character():
    
    def __init__(self, imgIn, posIn):
        self.image = imgIn
        self.pos = posIn

    def update(self):
        return

    def draw(self, target_surface):
        return

    def handle_click(self):
        return

    def contains_point(self, pt):
        # Use code from QueenSprite here
        return
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    #Load Game Resources  ##1
    spriteSheet = pygame.image.load("images//0x72_DungeonTilesetII_v1.3.png")
    
    #Load a knight
    knight = Character(spriteSheet,[200,200])

    # Create the ball object using it's position, size and color
    circle = Ball([50,100], 30, (255, 0, 0))        # A color is a mix of (Red, Green, Blue)
    
    circles = []
    for i in range(5):
        circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        
        #Move the circle
        #circle.pos[0] += 1  #TODO: Replace with with the move() method.
        circle.move(1,0)
        # Draw the circle on the surface
        circle.draw(mainSurface)
        
        for i in range(len(circles)):
            circles[i].move(1,0)
            circles[i].draw(mainSurface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
