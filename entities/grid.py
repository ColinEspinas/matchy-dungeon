import random
from typing import List
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.cell import Cell
from utils.cells import cellTypes, getRandomCellType
from components.shaker import Shaker

class Grid(Entity):

  def setup(self, options) -> None:
    self.size: Vector2 = Vector2(5, 6)
    self.cells: List[Cell] = []
    self.margin = 5
    self.cellSize = Vector2(40, 40)
    
    self.surface = pygame.Surface((
       self.size.x * (self.cellSize.x + self.margin),
       self.size.y * (self.cellSize.x + self.margin)
    ), pygame.SRCALPHA)

    self.shaker = self.components['shaker'] = Shaker(self, { 'surface': self.surface })

    self.layer = 'cells'

    self.transform.position.x = self.game.screen.get_width() / 2 - (self.size.x * (self.cellSize.x + self.margin) / 2)
    self.transform.position.y = self.game.screen.get_height() * 4.7 / 8 - (self.size.y * (self.cellSize.y + self.margin) / 2)
    self.generate()

  def generate(self) -> None:
    for row in range(int(self.size.y)):
      for col in range(int(self.size.x)):
        self.cells.append(None)

  def update(self, delta) -> None:
    for cell in range(len(self.cells)):
      self.dropCell(cell)
    self.generateNewCells()

  def getPositionFromCellIndex(self, index):
    return Vector2(
      int(index % self.size.x),
      int(index / self.size.x)
    )
  
  def getCellIndexFromPosition(self, position):
    return int(position.y * self.size.x + position.x)

  def getCellGroup(self, index, cellGroup):
    directions = [
      Vector2(0, 0),
      Vector2(0, -1),
      Vector2(0, 1),
      Vector2(-1, 0),
      Vector2(1, 0)
    ]
    cell = self.cells[index]
    if cell:
      cellPos = self.getPositionFromCellIndex(index)
      for direction in directions:
        # Get new pos from direction
        testedCellPos = Vector2(
          cellPos.x + direction.x,
          cellPos.y + direction.y
        )
        # Check if new pos is in grid
        if testedCellPos.x >= 0 and testedCellPos.x < self.size.x:
          if testedCellPos.y >= 1 and testedCellPos.y < self.size.y:
            testedCellIndex = self.getCellIndexFromPosition(testedCellPos)
            testedCell: Cell = self.cells[testedCellIndex]
            if testedCell:
              # Check if cell already in cellGroup
              if not any(testedCellIndex == c for c in cellGroup):
                # Check if cell is of same type
                if testedCell.type == cell.type:
                  cellGroup.append(testedCellIndex)
                  cellGroup = self.getCellGroup(testedCellIndex, cellGroup)
    return cellGroup

  def removeCell(self, index):
    for cellIndex in self.getCellGroup(index, []):
      cellPos = self.getPositionFromCellIndex(cellIndex)
      self.cells[cellIndex] = None
      self.game.removeEntity(f'cell-{int(cellPos.x)}-{int(cellPos.y)}')

  def dropCell(self, index):
    cell = self.cells[index]
    if cell:
      cellPos = self.getPositionFromCellIndex(index)
      cellPosBelow = Vector2(
        cellPos.x,
        cellPos.y + 1,
      )
      # Check if below pos is in grid
      if cellPosBelow.x >= 0 and cellPosBelow.x < self.size.x:
        if cellPosBelow.y >= 0 and cellPosBelow.y < self.size.y:
          cellIndexBelow = self.getCellIndexFromPosition(cellPosBelow)
          # Check if below cell is empty
          if not self.cells[cellIndexBelow]:
            self.cells[index] = None
            self.cells[cellIndexBelow] = cell
            cell.index = cellIndexBelow
            cell.targetPosition = Vector2(
              cellPosBelow.x * (self.cellSize.x + self.margin), 
              cellPosBelow.y * (self.cellSize.y + self.margin)
            )
            self.game.renameEntity(f'cell-{int(cellPos.x)}-{int(cellPos.y)}', f'cell-{int(cellPosBelow.x)}-{int(cellPosBelow.y)}')
            self.game.entities['player'].invalidateTargetCellGroup = True

  def generateNewCells(self):
    # For each column
    for cellIndex in range(int(self.size.x)):
      # Check if no cells on top of column
      if not self.cells[cellIndex]:
        # Add new cell
        newCellPos = self.getPositionFromCellIndex(cellIndex)
        newCell = Cell(self.game, {
          'index': cellIndex,
          'position': Vector2(
            newCellPos.x * (self.cellSize.x + self.margin), 
            newCellPos.y * (self.cellSize.y + self.margin)
          ),
          'size': self.cellSize,
          'type': getRandomCellType(),
          'grid': self
        })
        self.game.entities[f'cell-{int(newCellPos.x)}-{int(newCellPos.y)}'] = newCell
        self.cells[cellIndex] = newCell

  def getCellScreenPosition(self, index):
    cellPos = self.getPositionFromCellIndex(index)
    return Vector2(
      self.transform.position.x + cellPos.x * (self.cellSize.x + self.margin), 
      self.transform.position.y + cellPos.y * (self.cellSize.y + self.margin)
    )

  def resetGrid(self):
    for cell in range(len(self.cells)):
      self.removeCell(cell)