from core.component import Component

class Combo(Component):

  def setup(self, options) -> None:
    self.value = 1
    self.timer = 0
    self.maxTime = 3

  def update(self, delta) -> None:
    if self.timer > 0:
      self.timer -= delta
    else:
      self.value = 1

  def addToCombo(self, value):
    self.value += value
    self.timer = self.maxTime