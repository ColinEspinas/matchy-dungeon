import pygame
from pygame.locals import *
from pygame.math import Vector2
from components.combo import Combo

from core.entity import Entity
from entities.cell import Cell
from entities.dungeon import Dungeon
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
    self.dungeon: Dungeon = self.game.entities['dungeon']
    
    self.targetCellIndex = self.grid.getCellIndexFromPosition(Vector2(self.grid.size.x / 2, self.grid.size.y / 2))
    self.targetCell: Cell = self.grid.cells[self.targetCellIndex]

    self.targetCellGroup = self.grid.getCellGroup(self.targetCellIndex, [])
    self.invalidateTargetCellGroup = True

    self.transform.position = self.grid.getCellScreenPosition(self.targetCellIndex)
    self.target = self.transform.position

    self.layer = 'player'

    self.health = 10
    self.maxHealth = 10
    self.shield = 5
    self.maxShield = 10
    self.gold = 0

    self.flash = 0
    self.flashSurface = pygame.Surface(self.game.screen.get_size())
    self.flashColor = (255, 0, 0)

    self.combo = self.components['combo'] = Combo(self)

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
    if self.flash:
      self.flashSurface.fill(self.flashColor)
      self.flashSurface.set_alpha(32)
      self.game.screen.blit(self.flashSurface, (0, 0))

  def update(self, delta) -> None:
    if self.flash > 0:
      self.flash -= delta
    else:
      self.flash = 0
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
        self.action()
      self.invalidateTargetCellGroup = True

  def action(self):
    if self.targetCell:
      if self.targetCell.type == CellType.BASH:
        self.takeDamage(len(self.targetCellGroup))
      if self.targetCell.type == CellType.DEFENSE:
        self.setFlash(0.05, (self.targetCell.getCellColor()))
        self.shield = min(self.shield + len(self.targetCellGroup), self.maxShield)
      if self.targetCell.type == CellType.ATTACK:
        self.dealDamage(len(self.targetCellGroup))
      if self.targetCell.type == CellType.GOLD:
        self.gold += len(self.targetCellGroup)
      if not self.targetCell.type == CellType.PIKES:
        if not self.targetCell.type == CellType.EMPTY:
          if len(self.targetCellGroup) >= 3:
            self.combo.addToCombo(1)
          if len(self.targetCellGroup) >= 5:
            self.combo.addToCombo(1)
          if len(self.targetCellGroup) >= 10:
            self.combo.addToCombo(1)
        self.grid.removeCell(self.targetCellIndex)

  def movementAction(self):
    cell = self.grid.cells[self.targetCellIndex]
    if cell and cell.type == CellType.PIKES:
      self.takeDamage(1)

  def takeDamage(self, amount):
    self.setFlash()
    self.grid.shaker.shakeDuration += 0.1
    self.grid.shaker.shake += max(0.08, 0.02 * amount)
    if self.shield < amount:
      healthToRemove = amount - self.shield
      self.shield = 0
      self.health = max(0, self.health - healthToRemove)
    else:
      if self.shield > 0:
        self.shield = max(0, self.shield - amount)
      else:
        self.health = max(0, self.health - amount)

  def dealDamage(self, amount):
    self.setFlash(0.08, (255, 255, 255))
    monster = self.dungeon.monsters[self.dungeon.currentMonsterIndex]
    monster.shaker.shakeDuration += 0.1
    monster.shaker.shake += max(0.08, 0.06 * amount * max(1, self.combo.value))
    self.dungeon.attackCurrentMonster(amount * max(1, self.combo.value))

  def setFlash(self, duration = 0.1, color = (255, 0, 0)):
    self.flash = duration
    self.flashColor = color