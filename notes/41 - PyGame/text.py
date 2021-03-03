
import pygame
 
pygame.init()
mainSurface = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
 
 
def update_fps():

	return fps_text
 
 
loop = 1
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
			
	mainSurface.fill((0, 100, 0))
	
	words = "Hello Everyone!"
	renderedText = font.render(words, 1, pygame.Color("coral"))
	mainSurface.blit(renderedText, (10,0))

			
	
	pygame.display.flip()
 
pygame.quit()