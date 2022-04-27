from core.component import Component
from pygame import Vector2

class Transform(Component):

  def setup(self, options) -> None:
    self.position = Vector2(0, 0)
    self.velocity = Vector2(0, 0)
    if options:
      if 'position' in options: self.position = options['position']
      if 'velocity' in options: self.velocity = options['velocity']

  def update(self, delta) -> None:
    self.position.xy += self.velocity.xy * delta