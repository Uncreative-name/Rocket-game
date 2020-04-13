import pygame

from pygame.locals import *

pygame.init()

screen_info =  pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
screen.fill(color)

class ship:
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load("spaceRockets_003.png")
    self.rect = self.image.get_rect()
    self.image = pygame.transform.smoothscale(self.image, (int(0.4 * self.rect.width), int(0.4 * self.rect.height)))
    self.rect = self.image.get_rect()
    self.rect.center = pos

start = (30,300)
player = ship(start)

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    
    screen.blit(player.image, player.rect)

    pygame.display.flip()
  
if __name__ == "__main__":
  main()