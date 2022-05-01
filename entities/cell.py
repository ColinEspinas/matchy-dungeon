from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from utils.draw import cell
from utils.cells import CellType
class Cell(Entity):

  def setup(self, options) -> None:
    self.size = Vector2(10, 10)
    self.type = CellType.EMPTY
    self.grid = None
    self.index = 0
    self.layer = 'cells'
    self.duration = -1
    self.lifespan = 0
    if options:
      if 'index' in options: self.index = options['index']
      if 'position' in options: self.transform.position = options['position']
      if 'size' in options: self.size = options['size']
      if 'type' in options: self.type = options['type']
      if 'grid' in options: self.grid = options['grid']
    self.targetPosition = self.transform.position
    if self.type == CellType.PIKES:
      self.duration = 3
      self.lifespan = 0

  def update(self, delta) -> None:
    if self.duration > 0 and self.index > self.grid.size.x - 1:
      self.lifespan += delta
      if self.lifespan >= self.duration:
        self.lifespan = 0
        self.grid.removeCell(self.index)
    if self.transform.position != self.targetPosition:
      self.transform.position = self.transform.position.lerp(self.targetPosition, max(min(1, delta * 20), 0))

  def draw(self) -> None:
    inPlayerGroup = self.index in self.game.entities['player'].targetCellGroup
    cell(self.grid.surface, self, inPlayerGroup)

  def getCellColor(self):
    colors = {
      CellType.EMPTY: (49, 61, 90), # rgb(49, 61, 90)
      CellType.ATTACK: (219, 48, 105), # rgb(219, 48, 105)
      CellType.DEFENSE: (0, 232, 252), # rgb(0, 232, 252)
      CellType.GOLD: (255, 221, 74), # rgb(255, 221, 74)
      CellType.PIKES: (150, 164, 197), # rgb(150, 164, 197)
      CellType.BASH: (255, 98, 1), # rgb(255, 98, 1)
      # rgb(255, 98, 1)
      # rgb(49, 133, 252)
    }
    return colors[self.type]