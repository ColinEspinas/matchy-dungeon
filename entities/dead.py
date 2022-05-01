import pygame
from core.entity import Entity

class DeadMenu(Entity):
  def setup(self, options) -> None:
    self.layer = 'menu'
    self.openTimer = 0

  def update(self, delta) -> None:
    if self.openTimer > 0:
      self.openTimer -= delta

  def events(self, event, delta) -> None:
    if self.game.state == 'dead' and self.openTimer <= 0:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          grid = self.game.entities['grid']
          player = self.game.entities['player']
          dungeon = self.game.entities['dungeon']
          grid.resetGrid()
          dungeon.resetDungeon()
          player.health = player.maxHealth
          player.shield = 5
          player.gold = 0
          player.combo.value = 0
          grid.shaker.shake = 0
          self.game.state = 'game'

  def draw(self) -> None:
    if self.game.state == 'dead':
      pygame.draw.rect(self.game.screen, (14, 18, 26), (
        0, 0, self.game.screen.get_width(), self.game.screen.get_height()
      ))
      font = self.game.assets.fonts['regular']
      dungeon = self.game.entities['dungeon']
      floorText: pygame.Surface = font.render(f'You are dead at floor {dungeon.floor}.', False, (255, 255, 255))
      self.game.screen.blit(floorText, (
        self.game.screen.get_width() / 2 - floorText.get_width() / 2,
        self.game.screen.get_height() / 2 - 30
      ))
      deathText: pygame.Surface = font.render(f'Press SPACE to retry.', False, (255, 255, 255))
      self.game.screen.blit(deathText, (
        self.game.screen.get_width() / 2 - deathText.get_width() / 2,
        self.game.screen.get_height() / 2
      ))

  def openMenu(self):
    self.openTimer = 1