import pygame
from pygame.locals import *

pygame.init()

screen_info =  pygame.display.Info()
size = (width, height) = (int(screen_info.current_h), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (43, 56, 64)
screen.fill(color)


def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    pygame.display.flip()
  

if __name__ == "__main__":
  main()