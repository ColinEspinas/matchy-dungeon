import random
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.cell import Cell, CellType

class Grid(Entity):

  def __init__(self, entity, options = {}) -> None:
    self.size = Vector2(5, 5)
    self.cells = []
    self.margin = 5
    self.cellSize = Vector2(40, 40)
    super().__init__(entity, options)

  def setup(self, options) -> None:
    self.transform.position.x = self.game.screen.get_width() / 2 - (self.size.x * (self.cellSize.x + self.margin) / 2)
    self.transform.position.y = self.game.screen.get_height() / 2 - (self.size.y * (self.cellSize.y + self.margin) / 2)
    self.generate()

  def generate(self) -> None:
    cellTypes = [CellType.EMPTY, CellType.ATTACK, CellType.DEFENSE]
    for row in range(int(self.size.y)):
      for col in range(int(self.size.x)):
        self.cells.append(self.game.addEntity(f'cell-{row}-{col}', Cell(self.game, { 
          'position': Vector2(
            self.transform.position.x + col * (self.cellSize.x + self.margin), 
            self.transform.position.y + row * (self.cellSize.y + self.margin)
          ),
          'size': self.cellSize,
          'type': cellTypes[random.randint(0, 2)]
        })))

  def getPositionFromCellIndex(self, cell):
    return Vector2(
      int(cell % self.size.x),
      int(cell / self.size.x)
    )
  
  def getCellIndexFromPosition(self, position):
    return int(position.y * self.size.x + position.x)