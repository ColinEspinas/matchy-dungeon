import pygame
from pygame.math import Vector2

from core.game import Game
from entities.dungeon import Dungeon
from entities.grid import Grid
from entities.player_info import PlayerInfo
from entities.player import Player

game = Game({ 'title': 'Game', 'size': (1000, 600) }, 240, 1, ['default', 'cells', 'player', 'monster', 'ui'])

grid = game.addEntity('grid', Grid(game))
game.addEntity('dungeon', Dungeon(game))
game.addEntity('player', Player(game))
game.addEntity('health-bar', PlayerInfo(game, { 'position': Vector2(
  grid.transform.position.x,
  grid.transform.position.y + grid.size.y * (grid.cellSize.y + grid.margin)
) }))

game.run()