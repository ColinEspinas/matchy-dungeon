import sys, pygame
from pygame.locals import *
from core.assets import Assets

from core.entity import Entity

class Game:
  def __init__(self, windowOptions = {'title': 'Game', 'size': (400, 400)}, maxFramerate = 60, screenScale = 1, layers = ['default'], states = ['game']) -> None:
    # Define clock for update loop
    self.timer = pygame.time.Clock()
    # Define general game options
    self.windowOptions = windowOptions
    self.maxFramerate = maxFramerate
    # Create game window
    pygame.display.set_caption(self.windowOptions['title'])
    self.surf = pygame.display.set_mode(self.windowOptions['size'], 0, 32)
    # Prepare game screen
    self.screen = pygame.Surface((self.surf.get_width() / screenScale, self.surf.get_height() / screenScale))

    pygame.init()
    pygame.font.init()
    # Set states
    self.states = states
    self.state = self.states[0]
    # Declare game entities
    self.entities = {}
    # Declare layers
    self.layers = layers
    # Load assets
    self.assets = Assets()
    
  def addEntity(self, name: str, entity: Entity) -> Entity:
    if name not in self.entities:
      self.entities[name] = entity
      return entity

  def removeEntity(self, name: str) -> None:
    self.entities.pop(name)
  
  def renameEntity(self, oldName, newName):
    if oldName in self.entities:
      self.entities[newName] = self.entities.pop(oldName)

  def run(self) -> None:
    # pygame.joystick.init()
    # joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    # Game loop
    while True:
      # Get elapsed time and lock framerate
      elapsedTime = self.timer.tick(self.maxFramerate)
      delta = elapsedTime / 1000
      # Reset screen color
      self.screen.fill((14, 18, 26))
      # Event loop
      for event in pygame.event.get():
        for entity in list(self.entities.values()):
          entity.eventsComponents(event, delta)
          entity.events(event, delta)
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      # Update loop
      for entity in list(self.entities.values()):
          entity.updateComponents(delta)
          entity.update(delta)
      # Draw loop
      for layer in self.layers:
        for entity in list(self.entities.values()):
          if entity.layer == layer:
            entity.drawComponents()
            entity.draw()
      # Update pygame
      self.surf.blit(pygame.transform.scale(self.screen, (self.surf.get_size())), (0, 0))
      pygame.display.update()