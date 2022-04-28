import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.cell import Cell
from entities.grid import Grid
from utils.draw import cursor
from utils.cells import CellType

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
    self.targetCell: Cell = self.grid.cells[self.targetCellIndex]

    self.targetCellGroup = self.grid.getCellGroup(self.targetCellIndex, [])
    self.invalidateTargetCellGroup = True

    self.transform.position = self.targetCell.transform.position
    self.target = self.transform.position

    self.layer = 'player'

    self.health = 10
    self.maxHealth = 10
    self.shield = 5
    self.maxShield = 10
    self.gold = 0

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
    font = self.game.assets.fonts['regular']
    HealthText = font.render(f'HP={self.health}/{self.maxHealth} + {int(self.shield)}', False, (255, 255, 255))
    self.game.screen.blit(HealthText, (
      self.grid.transform.position.x,
      self.grid.transform.position.y + self.grid.size.y * (self.grid.cellSize.y + self.grid.margin)
    ))
    goldText = font.render(f'GOLD={self.gold}', False, (255, 255, 255))
    self.game.screen.blit(goldText, (
      self.grid.transform.position.x,
      self.grid.transform.position.y + self.grid.size.y * (self.grid.cellSize.y + self.grid.margin) + 30
    ))
    fpsText = font.render(f'FPS={int(self.game.timer.get_fps())}', False, (255, 255, 255))
    self.game.screen.blit(fpsText, (
      self.grid.transform.position.x,
      self.grid.transform.position.y + self.grid.size.y * (self.grid.cellSize.y + self.grid.margin) + 60
    ))

  def update(self, delta) -> None:
    self.shield = max(0, self.shield - delta / 2)
    self.targetCell = self.grid.cells[self.targetCellIndex]
    if self.targetCell:
      self.transform.position = self.transform.position.lerp(self.grid.getCellScreenPosition(self.targetCellIndex), max(min(1, delta * 20), 0))
      # Still not sure about the jaggy feeling of the next line
      # self.transform.position = self.transform.position.lerp(self.targetCell.transform.position, 0.1)
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
        self.movementAction()
      if event.key == self.keys['down'] and currentCellPosition.y < self.grid.size.y - 1:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x,
          currentCellPosition.y + 1,
        ))
        self.movementAction()
      if event.key == self.keys['left'] and currentCellPosition.x > 0:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x - 1,
          currentCellPosition.y,
        ))
        self.movementAction()
      if event.key == self.keys['right'] and currentCellPosition.x < self.grid.size.x - 1:
        self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(
          currentCellPosition.x + 1,
          currentCellPosition.y,
        ))
        self.movementAction()
      if event.key == self.keys['action']:
        # Do an action
        self.action()
      self.invalidateTargetCellGroup = True

  def action(self):
    if self.targetCell:
      if self.targetCell.type == CellType.BASH:
        self.takeDamage(len(self.targetCellGroup))
      if self.targetCell.type == CellType.DEFENSE:
        self.shield = min(self.shield + len(self.targetCellGroup), self.maxShield)
      if self.targetCell.type == CellType.GOLD:
        self.gold += len(self.targetCellGroup)
      if not self.targetCell.type == CellType.PIKES:
        # Remove cell
        self.grid.removeCell(self.targetCellIndex)

  def movementAction(self):
    cell = self.grid.cells[self.targetCellIndex]
    if cell and cell.type == CellType.PIKES:
      self.takeDamage(1)

  def takeDamage(self, amount):
    if self.shield > 0:
      self.shield = max(0, self.shield - amount)
    else:
      self.health = max(0, self.health - amount)