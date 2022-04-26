import pygame
from pygame.locals import *

from core.entity import Entity

class Player(Entity):

  width, height = 10, 100
  speed = 10

  keys = { 'up': pygame.K_UP, 'down': pygame.K_DOWN }

  collision = None

  def setup(self, options) -> None:
    if options:
      if 'position' in options: self.transform.position = options['position']
      if 'keys' in options: self.keys = options['keys']
    self.collision = pygame.Rect(self.transform.position.x, self.transform.position.y, self.width, self.height)
    print(self.transform.id)
    print(self.transform.velocity)

  def draw(self) -> None:
    pygame.draw.rect(self.game.screen, (100, 100, 100), self.collision)

  def update(self) -> None:
    keys = pygame.key.get_pressed();
    if keys[self.keys['up']]:
      self.transform.position.y -= self.speed
      if self.transform.position.y < -self.height:
        self.transform.position.y = self.game.screen.get_height()
    if keys[self.keys['down']]:
      self.transform.position.y += self.speed
      if self.transform.position.y > self.game.screen.get_height():
        self.transform.position.y = -self.height
    self.collision.x = self.transform.position.x
    self.collision.y = self.transform.position.y