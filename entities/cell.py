from enum import Enum
import pygame
from pygame.locals import *
from pygame.math import Vector2

from core.entity import Entity

class CellType(Enum):
  EMPTY = 0
  ATTACK = 1
  DEFENSE = 2

class Cell(Entity):

  def __init__(self, entity, options = {}) -> None:
    self.size = Vector2(10, 10)
    self.type = CellType.EMPTY
    super().__init__(entity, options)

  def setup(self, options) -> None:
    if options:
      if 'position' in options: self.transform.position = options['position']
      if 'size' in options: self.size = options['size']
      if 'type' in options: self.type = options['type']

  def draw(self) -> None:
    pygame.draw.rect(
      self.game.screen,
      self.getCellColor(),
      (self.transform.position.x, self.transform.position.y, self.size.x, self.size.y),
      4, 6
    )

  def getCellColor(self):
    colors = {
      CellType.EMPTY: (49, 61, 90),
      CellType.ATTACK: (219, 48, 105),
      CellType.DEFENSE: (0, 232, 252)
    }
    return colors[self.type]
  # def rectRotated(self, surface, color, pos, fill, border_radius, rotation_angle, rotation_center = (0,0), nAntialiasingRatio = 1 ):
  #   nRenderRatio = nAntialiasingRatio

  #   sw = pos[2] + abs(rotation_center[0]) * 2
  #   sh = pos[3] + abs(rotation_center[1]) * 2

  #   surfcenterx = sw//2
  #   surfcentery = sh//2
  #   s = pygame.Surface( (sw*nRenderRatio,sh*nRenderRatio) )
  #   s = s.convert_alpha()
  #   s.fill((0,0,0,0))

  #   rw2=pos[2]//2 # halfwidth of rectangle
  #   rh2=pos[3]//2

  #   pygame.draw.rect( s, color, ((surfcenterx-rw2-rotation_center[0])*nRenderRatio,(surfcentery-rh2-rotation_center[1])*nRenderRatio,pos[2]*nRenderRatio,pos[3]*nRenderRatio), fill*nRenderRatio, border_radius=border_radius*nRenderRatio )
  #   s = pygame.transform.rotate( s, rotation_angle )        
  #   if nRenderRatio != 1: s = pygame.transform.smoothscale(s,(s.get_width()//nRenderRatio,s.get_height()//nRenderRatio))
  #   incfromrotw = (s.get_width()-sw)//2
  #   incfromroth = (s.get_height()-sh)//2
  #   surface.blit( s, (pos[0]-surfcenterx+rotation_center[0]+rw2-incfromrotw,pos[1]-surfcentery+rotation_center[1]+rh2-incfromroth) )