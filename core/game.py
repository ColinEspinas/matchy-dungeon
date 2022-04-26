import sys, pygame
from pygame.locals import *

from core.entity import Entity

class Game:
  def __init__(self, windowOptions = {'title': 'Game', 'size': (400, 400)}) -> None:
    # Define clock for update loop
    self.timer = pygame.time.Clock()
    # Define general game options
    self.windowOptions = windowOptions
    # Create game window
    pygame.display.set_caption(self.windowOptions['title'])
    self.screen = pygame.display.set_mode(self.windowOptions['size'], 0, 32)
    # Declare game entities
    self.entities = {}
    
  def addEntity(self, name: str, entity: Entity) -> Entity:
    if name not in self.entities:
      self.entities[name] = entity
      return entity

  def run(self) -> None:
    pygame.init()
    # Game loop
    while True:
      # Reset screen color
      self.screen.fill((0, 0, 0))
      # Event loop
      for event in pygame.event.get():
        for entity in self.entities.values():
          entity.eventsComponents(event)
          entity.events(event)
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      # Update loop
      for entity in self.entities.values():
          entity.updateComponents()
          entity.update()
      # Draw loop
      for entity in self.entities.values():
          entity.drawComponents()
          entity.draw()
      # Update pygame
      pygame.display.update()
      self.timer.tick(60)