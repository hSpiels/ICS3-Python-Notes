import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Move the Dino
        wizardPos[0] += 0.5   #update the x for the lizard
        lizardPos[0] += 0.5   #update the x for the wizard
        
        #Draw the whole sheet
        #mainSurface.blit(spriteSheet, lizardPos)
        
        #Kinda fun to have EVERY Image, but let's just get the patches we need
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint
        mainSurface.blit(spriteSheet, lizardPos, [127,236,16,28])  #Positions found using msPaint
        
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
