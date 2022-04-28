from __future__ import annotations
from math import sin
from typing import TYPE_CHECKING

import pygame
from utils.cells import CellType

if TYPE_CHECKING:
  from entities.cell import Cell

def cursor(surface, color, position, radius, size, width):
  pygame.draw.circle(
    surface,
    color,
    (position.x + size.x / 2 + size.x / 4, position.y + size.y / 2 - size.y / 4),
    radius,
    width,
    True, False, False, False
  )
  pygame.draw.circle(
    surface,
    color,
    (position.x + size.x / 2 - size.x / 4, position.y + size.y / 2 - size.y / 4),
    radius,
    width,
    False, True, False, False
  )
  pygame.draw.circle(
    surface,
    color,
    (position.x + size.x / 2 - size.x / 4, position.y + size.y / 2 + size.y / 4),
    radius,
    width,
    False, False, True, False
  )
  pygame.draw.circle(
    surface,
    color,
    (position.x + size.x / 2 + size.x / 4, position.y + size.y / 2 + size.y / 4),
    radius,
    width,
    False, False, False, True,
  )

def cell(surface, cell: Cell, inPlayerGroup):
    surf = pygame.Surface((cell.size.x, cell.size.y), pygame.SRCALPHA)
    if not cell.index < cell.grid.size.x:
      if inPlayerGroup:
        rect = pygame.Surface((cell.size.x, cell.size.y), pygame.SRCALPHA)
        pygame.draw.rect(rect, cell.getCellColor(), (0, 0, cell.size.x, cell.size.y), 0, 6)
        rect.set_alpha(164)
        surf.blit(rect, (0, 0), None, pygame.BLEND_ALPHA_SDL2)
        pygame.draw.rect(surf, cell.getCellColor(), (0, 0, cell.size.x, cell.size.y), 4, 6)
      else:
        pygame.draw.rect(surf, cell.getCellColor(), (0, 0, cell.size.x, cell.size.y), 4, 6)
      if cell.type == CellType.ATTACK: sword(surf, cell)
      if cell.type == CellType.DEFENSE: shield(surf, cell)
      if cell.type == CellType.GOLD: coin(surf, cell)
      if cell.type == CellType.BASH: skull(surf, cell)
      if cell.type == CellType.PIKES: pike(surf, cell)
    if cell.index < cell.grid.size.x:
      pygame.draw.rect(
        surf,
        cell.getCellColor(),
        (cell.size.x / 4, cell.size.x / 4, cell.size.x / 2, cell.size.y / 2),
        4, 6
      )
    if not inPlayerGroup:
      surf.set_alpha(200)
      if cell.index < cell.grid.size.x:
        surf.set_alpha(200)
    surface.blit(surf, (cell.transform.position.x, cell.transform.position.y), None, pygame.BLEND_ALPHA_SDL2)

def shield(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['shield'], (cell.size.x - 10, cell.size.y - 10))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())
  surface.blit(arr.make_surface(), (4.5, 3))

def sword(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['sword'], (cell.size.x - 10, cell.size.y - 10))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())
  surface.blit(arr.make_surface(), (5, 4), None, pygame.BLEND_ALPHA_SDL2)

def coin(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['coin'], (cell.size.x - 10, cell.size.y - 10))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())
  surface.blit(arr.make_surface(), (5, 5), None, pygame.BLEND_ALPHA_SDL2)

def fist(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['fist'], (cell.size.x - 10, cell.size.y - 10))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())
  surface.blit(arr.make_surface(), (5, 4), None, pygame.BLEND_ALPHA_SDL2)

def pike(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['pike'], (cell.size.x - 20, cell.size.y - 0))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())  
  surface.blit(arr.make_surface(), (1, 12), None, pygame.BLEND_ALPHA_SDL2)
  surface.blit(arr.make_surface(), (10, 12), None, pygame.BLEND_ALPHA_SDL2)
  surface.blit(arr.make_surface(), (19, 12), None, pygame.BLEND_ALPHA_SDL2)

def skull(surface: pygame.Surface, cell: Cell):
  image = pygame.transform.scale(cell.game.assets.images['skull'], (cell.size.x - 10, cell.size.y - 10))
  arr = pygame.PixelArray(image)
  arr.replace((0, 0, 0), cell.getCellColor())
  surf = arr.make_surface()
  surface.blit(surf, (5, 5), None, pygame.BLEND_ALPHA_SDL2)