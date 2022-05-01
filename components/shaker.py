import random

from pygame import Vector2
import pygame
from core.component import Component

class Shaker(Component):

  def setup(self, options) -> None:
    self.shake = 0
    self.shakeRestore = 0.2
    self.shakeDuration = 0
    self.maxShakeAngle = 30
    self.maxShakeOffset = 10

    self.surface = None
    if options:
      if 'surface' in options: self.surface = options['surface']

  def update(self, delta) -> None:
    if self.shakeDuration > 0:
      self.shakeDuration -= delta
    else: 
      if self.shake > 0:
        self.shake -= delta * self.shakeRestore
      else:
        self.shake = 0

  def draw(self) -> None:
      shake = self.getShake(self.shake)
      self.entity.game.screen.blit(pygame.transform.rotate(self.surface, shake[1]), (shake[0].x, shake[0].y), None, pygame.BLEND_ALPHA_SDL2)
      self.surface.fill(0)

  def getShake(self, shake):
    angle = self.maxShakeAngle * shake * random.uniform(-1, 1)
    offset = Vector2(self.maxShakeOffset * shake * random.uniform(-1, 1), self.maxShakeOffset * shake * random.uniform(-1, 1))
    return (self.entity.transform.position + offset, angle)