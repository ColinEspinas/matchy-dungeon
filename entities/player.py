from math import sin
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.cell import Cell
from entities.grid import Grid

class Player(Entity):

  keys = { 
    'up': pygame.K_UP, 
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
  }

  def setup(self, options) -> None:
    self.size = Vector2(40, 40)
    self.grid = self.game.entities['grid']
    self.targetCellIndex = 0
    self.targetCell = self.grid.cells[self.targetCellIndex]
    self.transform.position = self.targetCell.transform.position
    self.target = self.transform.position
    if options:
      if 'position' in options: self.transform.position = options['position']
      if 'keys' in options: self.keys = options['keys']

  def draw(self) -> None:
    radius = self.size.x / 2 - 6
    pygame.draw.circle(
      self.game.screen,
      (255, 255, 255),
      (self.transform.position.x + self.size.x / 2 + self.size.x / 4, self.transform.position.y + self.size.y / 2 - self.size.y / 4),
      radius,
      4,
      True, False, False, False
    )
    pygame.draw.circle(
      self.game.screen,
      (255, 255, 255),
      (self.transform.position.x + self.size.x / 2 - self.size.x / 4, self.transform.position.y + self.size.y / 2 - self.size.y / 4),
      radius,
      4,
      False, True, False, False
    )
    pygame.draw.circle(
      self.game.screen,
      (255, 255, 255),
      (self.transform.position.x + self.size.x / 2 - self.size.x / 4, self.transform.position.y + self.size.y / 2 + self.size.y / 4),
      radius,
      4,
      False, False, True, False
    )
    pygame.draw.circle(
      self.game.screen,
      (255, 255, 255),
      (self.transform.position.x + self.size.x / 2 + self.size.x / 4, self.transform.position.y + self.size.y / 2 + self.size.y / 4),
      radius,
      4,
      False, False, False, True,
    )

  def update(self, delta) -> None:
    self.targetCell = self.grid.cells[self.targetCellIndex]
    self.transform.position = self.transform.position.lerp(self.targetCell.transform.position, 0.1)

  def events(self, event, delta) -> None:
    if event.type == KEYDOWN:
      currentCellPosition = self.grid.getPositionFromCellIndex(self.targetCellIndex)
      if event.key == self.keys['up'] and currentCellPosition.y > 0:
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