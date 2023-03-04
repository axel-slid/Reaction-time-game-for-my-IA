import pygame, sys
from pygame.locals import QUIT

import random
import time
import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Reaction Time Game")

# Create a red box
box = pygame.Surface((50, 50))
box.fill((255, 0, 0))

# Initialize time variables
start_time = 0
end_time = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(box, (125, 125))
    pygame.display.flip()

    # Wait for a random amount of time
    wait_time = random.uniform(0.5, 2.5)
    time.sleep(wait_time)
  
    
    # Change the box to green
    box.fill((0, 255, 0))
    screen.blit(box, (125, 125))
    pygame.display.flip()

    start_time = time.time()

    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                end_time = time.time()
                waiting = False
              
    reaction_time = (end_time - start_time - 0.2)*1000
    print(reaction_time)
  


    font = pygame.font.Font(None, 30)
    if reaction_time >= 0.01:
      text = font.render("Reaction Time: {:.2f} ms".format(reaction_time), True, (0, 0, 0))
      text_rect = text.get_rect()
      text_rect.center = (150, 150)
      screen.blit(text, text_rect)
      pygame.display.flip()
  
     
      time.sleep(1)
  
      # Change the box back to red
      box.fill((255, 0, 0))
    else:
      text = font.render("You're too soon!", True, (0, 0, 0))
      text_rect = text.get_rect()
      text_rect.center = (150, 150)
      screen.blit(text, text_rect)
      pygame.display.flip()
  
     
      time.sleep(1)
      box.fill((255, 0, 0))

# Quit pygame
pygame.quit()