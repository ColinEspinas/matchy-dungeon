import pygame
from pygame.locals import *
from pygame.math import Vector2
from components.shaker import Shaker

from core.entity import Entity
from utils.draw import monster

class Monster(Entity):

  def setup(self, options) -> None:
    self.index = 0
    self.dungeon = None
    self.size = Vector2(40, 40)

    self.name = 'Unnamed monster'
    self.maxHealth = self.health = 10
    
    self.surface = pygame.Surface((
       self.size.x,
       self.size.y
    ), pygame.SRCALPHA)
    self.shaker = self.components['shaker'] = Shaker(self, { 'surface': self.surface })

    self.layer = 'monster'

    self.inCombatPosition = Vector2(0, 0)

    if 'index' in options: self.index = options['index']
    if 'position' in options: self.inCombatPosition = options['position']
    if 'dungeon' in options: self.dungeon = options['dungeon']
    if 'size' in options: self.size = options['size']
    if 'health' in options: self.maxHealth = self.health = options['health']

    self.transform.position = self.getWaitingPosition()
  
  def update(self, delta) -> None:
    if self.dungeon.currentMonsterIndex == self.index:
      if self.transform.position != self.inCombatPosition:
        self.transform.position = self.transform.position.lerp(self.inCombatPosition, max(min(1, delta * 20), 0))
    else:
      if self.transform.position != self.getWaitingPosition():
        self.transform.position = self.transform.position.lerp(self.getWaitingPosition(), max(min(1, delta * 20), 0))
    pass

  def draw(self) -> None:
    self.surface = monster(self.game.screen, self)
    self.shaker.surface = self.surface
    if self.dungeon.currentMonsterIndex == self.index:
      font = self.game.assets.fonts['regular']
      healthText = font.render(f'{self.health}/{self.maxHealth}', False, (255, 255, 255))
      healthTextScaled = pygame.transform.scale(healthText, (
        healthText.get_width() / 1.4,
        healthText.get_height() / 1.4
      ))
      self.game.screen.blit(healthTextScaled, (
        (self.transform.position.x + self.size.x / 2) - healthTextScaled.get_width() / 2,
        self.transform.position.y + self.size.y + 5
      ))

  def takeDamage(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.die()

  def die(self):
    self.dungeon.killMonster(self.index)

  def getWaitingPosition(self):
    return Vector2(
      self.inCombatPosition.x + self.size.x / 2 + (self.index - self.dungeon.currentMonsterIndex) * (self.size.x / 2 + 5),
      self.inCombatPosition.y + self.size.y / 2
    )