import pygame
import math

class ship:
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load("Player.png")
    self.image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()
    self.image = pygame.transform.smoothscale(self.image, (int(0.4 * self.rect.width), int(0.4 * self.rect.height)))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0, 0)
  def update(self):
    self.rect.move_ip(self.speed)

    if self.rect.left < 0:
      self.rect.move_ip(-self.speed)
      self.speed[0] = 0
    
    if self.rect.top < 0:
      self.rect.move_ip(-self.speed)
      self.speed[0] = 0