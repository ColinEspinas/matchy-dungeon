from __future__ import annotations
from typing import TYPE_CHECKING, Dict

import uuid

from components.transform import Transform

if TYPE_CHECKING:
  from core.game import Game
  from core.component import Component

class Entity:
  def __init__(self, game: Game, options: Dict) -> None:
    self.id = uuid.uuid4()
    self.game = game
    self.components: Dict[str, Component] = {
      'transform': Transform(self)
    }
    self.transform = self.components['transform']
    self.setup(options)

  def setup(self, options) -> None:
    pass

  def events(self, event) -> None:
    pass

  def update(self) -> None:
    pass

  def draw(self) -> None:
    pass

  def eventsComponents(self, event) -> None:
    for component in self.components.values():
      component.events(event)

  def updateComponents(self) -> None:
    for component in self.components.values():
      component.update()

  def drawComponents(self) -> None:
    for component in self.components.values():
      component.draw()