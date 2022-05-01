import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.grid import Grid
from entities.monster import Monster
from utils.draw import player

class Dungeon(Entity):

  def setup(self, options) -> None:
    grid: Grid = self.game.entities['grid']
    self.size = Vector2(
      grid.size.x * (grid.cellSize.x + grid.margin),
      150
    )

    self.floor = 5
    self.monsters = []
    self.currentMonsterIndex = 0

    self.layer = 'default'

    self.transform.position.x = self.game.screen.get_width() / 2 - (self.size.x / 2)
    self.transform.position.y = 30

    self.generateFloor()

  def generateFloor(self):
    self.clearFloor()
    if self.floor == 0:
      self.monsters = [self.generateMonster(0)]
    elif self.floor < 5:
      for i in range(3):
        self.monsters.append(self.generateMonster(i))
    elif self.floor < 10:
      for i in range(5):
        self.monsters.append(self.generateMonster(i))
    elif self.floor < 20:
      for i in range(10):
        self.monsters.append(self.generateMonster(i))
    elif self.floor < 50:
      for i in range(15):
        self.monsters.append(self.generateMonster(i))
    elif self.floor < 100:
      for i in range(25):
        self.monsters.append(self.generateMonster(i))
    else:
      for i in range(50):
        self.monsters.append(self.generateMonster(i))
    print(f'current floor: {self.floor}', self.monsters)
  
  def generateMonster(self, index):
    return self.game.addEntity(f'monster-{index}', Monster(self.game, {
      'index': index,
      'position': Vector2(
        self.transform.position.x + self.size.x - 90,
        self.transform.position.y + self.size.y / 1.5 - 20
      ),
      'size': Vector2(40, 40),
      'dungeon': self
    }))

  def clearFloor(self):
    for i in range(len(self.monsters)):
      self.game.removeEntity(f'monster-{i}')
    self.monsters = []

  def attackCurrentMonster(self, amount):
    monster: Monster = self.monsters[self.currentMonsterIndex]
    monster.takeDamage(amount)

  def killMonster(self, index):
    self.monsters[index] = None
    if self.currentMonsterIndex >= len(self.monsters) - 1:
      self.floor += 1
      self.currentMonsterIndex = 0
      self.generateFloor()
    else:
      self.currentMonsterIndex += 1

  def draw(self) -> None:
    pygame.draw.rect(self.game.screen, (20, 24, 36), (
      self.transform.position.x - 10,
      self.transform.position.y + 50,
      self.size.x + 20,
      self.size.y - 50
    ), 0, 6)
    player(self.game.screen, self.game.assets, Vector2(
      self.transform.position.x + 43,
      self.transform.position.y + self.size.y / 1.5 - 20
      ), Vector2(40, 40))
    font = self.game.assets.fonts['regular']
    floorText = font.render(f'floor={self.floor}', False, (255, 255, 255))
    self.game.screen.blit(floorText, (
      self.transform.position.x,
      self.transform.position.y
    ))