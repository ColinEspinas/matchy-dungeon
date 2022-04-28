from enum import Enum
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity

class CellType(Enum):
  EMPTY = 0
  ATTACK = 1
  DEFENSE = 2
  GOLD = 3
  PIKES = 4
  BASH = 5

class Cell(Entity):

  cellTypes = [
    CellType.EMPTY, 
    CellType.ATTACK, 
    CellType.DEFENSE, 
    CellType.GOLD, 
    CellType.PIKES, 
    CellType.BASH
  ]

  def setup(self, options) -> None:
    self.size = Vector2(10, 10)
    self.type = CellType.EMPTY
    self.grid = None
    self.index = 0
    self.layer = 'cells'
    if options:
      if 'index' in options: self.index = options['index']
      if 'position' in options: self.transform.position = options['position']
      if 'size' in options: self.size = options['size']
      if 'type' in options: self.type = options['type']
      if 'grid' in options: self.grid = options['grid']
    self.targetPosition = self.transform.position

  def update(self, delta) -> None:
    self.transform.position = self.transform.position.lerp(self.targetPosition, 0.05)

  def draw(self) -> None:
    inPlayerGroup = self.index not in self.game.entities['player'].targetCellGroup
    surf = pygame.Surface((self.size.x, self.size.y), pygame.SRCALPHA)
    if not self.index < self.grid.size.x:
      if inPlayerGroup:
        pygame.draw.rect(surf, self.getCellColor(), (0, 0, self.size.x, self.size.y), 4, 6)
      else:
        pygame.draw.rect(surf, self.getCellColor(), (0, 0, self.size.x, self.size.y), 0, 6)
    if self.index < self.grid.size.x:
      pygame.draw.rect(
        surf,
        self.getCellColor(),
        (self.size.x / 4, self.size.x / 4, self.size.x / 2, self.size.y / 2),
        4, 6
      )
    if self.index not in self.game.entities['player'].targetCellGroup:
      if not self.index < self.grid.size.x:
        surf.set_alpha(200)
      else:
        surf.set_alpha(200)
    self.game.screen.blit(surf, (self.transform.position.x, self.transform.position.y), None, pygame.BLEND_ALPHA_SDL2)

  def getCellColor(self):
    colors = {
      CellType.EMPTY: (49, 61, 90), # rgb(49, 61, 90)
      CellType.ATTACK: (0, 232, 252), # rgb(0, 232, 252)
      CellType.DEFENSE: (49, 133, 252), # rgb(49, 133, 252)
      CellType.GOLD: (255, 221, 74), # rgb(255, 221, 74)
      CellType.PIKES: (150, 164, 197), # rgb(150, 164, 197)
      CellType.BASH: (219, 48, 105), # rgb(219, 48, 105)
      # 236, 117, 5
    }
    return colors[self.type]