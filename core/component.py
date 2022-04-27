from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from core.entity import Entity

import uuid

class Component:
  def __init__(self, entity: Entity, options = {}) -> None:
    self.id = uuid.uuid4()
    self.entity = entity
    self.setup(options)

  def setup(self, options) -> None:
    pass

  def draw(self) -> None:
    pass

  def update(self, delta) -> None:
    pass

  def events(self, event, delta) -> None:
    pass