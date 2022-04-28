from __future__ import annotations
from typing import TYPE_CHECKING, Dict

import uuid

from components.transform import Transform

if TYPE_CHECKING:
  from core.game import Game
  from core.component import Component

class Entity:
  def __init__(self, game: Game, options = {}) -> None:
    self.id = uuid.uuid4()
    self.game = game
    self.components: Dict[str, Component] = {
      'transform': Transform(self)
    }
    self.transform: Transform = self.components['transform']
    self.layer = 'default'
    self.setup(options)

  def setup(self, options) -> None:
    pass

  def events(self, event, delta) -> None:
    pass

  def update(self, delta) -> None:
    pass

  def draw(self) -> None:
    pass

  def eventsComponents(self, event, delta) -> None:
    for component in self.components.values():
      component.events(event, delta)

  def updateComponents(self, delta) -> None:
    for component in self.components.values():
      component.update(delta)

  def drawComponents(self) -> None:
    for component in self.components.values():
      component.draw()