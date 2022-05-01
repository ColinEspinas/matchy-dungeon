from math import ceil
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity
from entities.player import Player
from utils.draw import healthIcon, shieldIcon, goldIcon


class PlayerInfo(Entity):

  def setup(self, options) -> None:
    self.player: Player = self.game.entities['player']
    self.size = Vector2()
    self.margin = 5
    self.layer = 'ui'
    if options:
      if 'position' in options: self.transform.position = options['position']
      if 'size' in options: self.size = options['size']

  def draw(self) -> None:
    # Heart info
    healthIcon(self.game.screen, self.game.assets, self.transform.position, Vector2(30, 30), (255, 0, 0))
    font = self.game.assets.fonts['regular']
    healthText = font.render(f'{self.player.health}/{self.player.maxHealth}', False, (255, 255, 255))
    self.game.screen.blit(healthText, (
      self.transform.position.x + 30 + self.margin,
      self.transform.position.y + 2
    ))
    # Shield info
    shieldIcon(self.game.screen, self.game.assets, Vector2(
      self.transform.position.x + healthText.get_width() + (30 + self.margin) + self.margin, 
      self.transform.position.y
    ), Vector2(30, 30), (0, 232, 252))
    shieldText = font.render(f'{ceil(self.player.shield)}/{self.player.maxShield}', False, (255, 255, 255))
    self.game.screen.blit(shieldText, (
      self.transform.position.x + healthText.get_width() + (30 + self.margin) * 2 + self.margin,
      self.transform.position.y + 2
    ))
    # Gold info
    goldIcon(self.game.screen, self.game.assets, Vector2(
      self.transform.position.x, 
      self.transform.position.y + 30
    ), Vector2(30, 30), (255, 221, 74))
    goldText = font.render(f'{self.player.gold}', False, (255, 255, 255))
    self.game.screen.blit(goldText, (
      self.transform.position.x + 30 + self.margin,
      self.transform.position.y + 2 + 30
    ))
    if self.player.combo.value > 1:
      comboFont = self.game.assets.fonts['big-regular']
      comboText = comboFont.render(f'x{self.player.combo.value}', False, (255, 255, 255))
      self.game.screen.blit(pygame.transform.rotate(comboText, -15), (
        self.transform.position.x + self.player.grid.surface.get_width() + self.player.grid.margin,
        self.player.grid.transform.position.y + self.player.grid.cellSize.y + self.player.grid.margin
      ))