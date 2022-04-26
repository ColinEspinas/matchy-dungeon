from core.component import Component
from pygame import Vector2

class Transform(Component):

  def __init__(self, entity, options = {}) -> None:
    self.position = Vector2(0, 0)
    self.velocity = Vector2(0, 0)
    super().__init__(entity, options)

  def setup(self, options) -> None:
    if options:
      if 'position' in options: self.position = options['position']
      if 'velocity' in options: self.velocity = options['velocity']

  def update(self) -> None:
    self.position.xy += self.velocity.xy