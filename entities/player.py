from math import sin
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.cell import Cell
from entities.grid import Grid
from utils.draw import cursor

class Player(Entity):

  keys = { 
    'up': pygame.K_UP, 
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'action': pygame.K_SPACE,
  }

  def setup(self, options) -> None:
    self.size = Vector2(40, 40)
    self.grid: Grid = self.game.entities['grid']
    
    self.targetCellIndex = int(self.grid.size.x)
    self.targetCell = self.grid.cells[self.targetCellIndex]

    self.targetCellGroup = self.grid.getCellGroup(self.targetCellIndex, [])
    self.invalidateTargetCellGroup = True

    self.transform.position = self.targetCell.transform.position
    self.target = self.transform.position

    self.layer = 'player'

    if options:
      if 'position' in options: self.transform.position = options['position']
      if 'keys' in options: self.keys = options['keys']

  def draw(self) -> None:
    radius = self.size.x / 2 - 6
    cursor(
      self.game.screen,
      (255, 255, 255),
      self.transform.position,
      radius,
      self.size,
      4
    )

  def update(self, delta) -> None:
    self.targetCell = self.grid.cells[self.targetCellIndex]
    if self.targetCell:
      self.transform.position = self.transform.position.lerp(self.targetCell.transform.position, 0.1)
    if self.invalidateTargetCellGroup:
      self.targetCellGroup = self.grid.getCellGroup(self.targetCellIndex, [])
      self.invalidateTargetCellGroup = False

  def events(self, event, delta) -> None:
    if event.type == KEYDOWN:
      currentCellPosition = self.grid.getPositionFromCellIndex(self.targetCellIndex)
      if event.key == self.keys['up'] and currentCellPosition.y > 1:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x,
          currentCellPosition.y - 1,
        ))
      if event.key == self.keys['down'] and currentCellPosition.y < self.grid.size.y - 1:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x,
          currentCellPosition.y + 1,
        ))
      if event.key == self.keys['left'] and currentCellPosition.x > 0:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x - 1,
          currentCellPosition.y,
        ))
      if event.key == self.keys['right'] and currentCellPosition.x < self.grid.size.x - 1:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x + 1,
          currentCellPosition.y,
        ))
      if event.key == self.keys['action']:
        # Remove cell
        self.grid.removeCell(self.targetCellIndex)
      self.invalidateTargetCellGroup = True