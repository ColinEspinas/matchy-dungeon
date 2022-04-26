import random
import pygame
from core.entity import Entity
from pygame.math import Vector2

class Ball(Entity):

  radius = 6
  speed = initialSpeed = 5
  collision = None

  def setup(self, options) -> None:
    # if options:
      # if 'position' in options: self.transform.position = options['position']
    self.collision = pygame.Rect(
      self.transform.position.x - self.radius / 2,
      self.transform.position.y - self.radius / 2,
      self.radius,
      self.radius
    )
    self.transform.velocity.x = self.speed

  def draw(self) -> None:
    pygame.draw.circle(
      self.game.screen,
      (255, 0, 100),
      (self.transform.position.x, self.transform.position.y),
      self.radius
    )

  def update(self) -> None:
    self.collision.x = self.transform.position.x - self.radius / 2
    self.collision.y = self.transform.position.y - self.radius / 2

    player1 = self.game.entities['player1']
    player2 = self.game.entities['player2']

    if self.collision.colliderect(player1.collision):
      self.transform.velocity.x = self.speed
      self.transform.velocity.y = random.randint(-self.initialSpeed, self.initialSpeed)
      self.speed += 1
    
    if self.collision.colliderect(player2.collision):
      self.transform.velocity.x = -self.speed
      self.transform.velocity.y = random.randint(-self.initialSpeed, self.initialSpeed)
      self.speed += 1

    if self.transform.position.y > self.game.screen.get_height() or self.transform.position.y < 0:
      self.transform.velocity.y = -self.transform.velocity.y

    if self.transform.position.x < 0 or self.transform.position.x > self.game.screen.get_width():
      self.transform.position = Vector2(self.game.screen.get_width() / 2 - 3, self.game.screen.get_height() / 2 - 3)
      randomDir = random.randint(-1, 1) or 1
      self.transform.velocity.x =  randomDir * self.speed
      self.transform.velocity.y = 0
      self.speed = 5
    pass