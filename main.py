import pygame
from Ship import ship


from pygame.locals import *

pygame.init()

screen_info =  pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
screen.fill(color)

start = (80,300)
player = ship(start)

asteroids = pygame.sprite.Group()

level = 1

def main():
  
  while True:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_RIGHT:
          player.speed[0] += 1
        
        if event.key == pygame.K_LEFT:
          player.speed[0] -= 1
        
        if event.key == pygame.K_UP:
          player.speed[1] -= 1
        
        if event.key == pygame.K_DOWN:
          player.speed[1] += 1
        
        if event.key == pygame.K_SPACE:
          player.speed[0] += 6
  


    player.update()
    screen.fill(color)
    
    screen.blit(player.image, player.rect)

    pygame.display.flip()
  
if __name__ == "__main__":
  main()