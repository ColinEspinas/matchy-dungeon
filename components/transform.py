from core.component import Component
from utils.vector import Vector

class Transform(Component):

  position = Vector(0, 0)
  velocity = Vector(0, 0)

  def setup(self, options) -> None:
    if options:
      if 'position' in options: self.position = options['position']
      if 'velocity' in options: self.velocity = options['velocity']

  def update(self) -> None:
    self.position.x += self.velocity.x
    self.position.y += self.velocity.y