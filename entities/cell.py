from enum import Enum
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity

class CellType(Enum):
  EMPTY = 0
  ATTACK = 1
  DEFENSE = 2

class Cell(Entity):

  def setup(self, options) -> None:
    self.size = Vector2(10, 10)
    self.type = CellType.EMPTY
    self.index = 0
    if options:
      if 'index' in options: self.index = options['index']
      if 'position' in options: self.transform.position = options['position']
      if 'size' in options: self.size = options['size']
      if 'type' in options: self.type = options['type']

  def draw(self) -> None:
    surf = pygame.Surface((self.size.x, self.size.y))
    pygame.draw.rect(
      surf,
      self.getCellColor(),
      (0, 0, self.size.x, self.size.y),
      4, 6
    )
    if self.game.entities['player'].targetCellIndex != self.index:
      surf.set_alpha(128)
    self.game.screen.blit(surf, (self.transform.position.x, self.transform.position.y))

  def getCellColor(self):
    colors = {
      CellType.EMPTY: (49, 61, 90),
      CellType.ATTACK: (219, 48, 105),
      CellType.DEFENSE: (0, 232, 252)
    }
    return colors[self.type]