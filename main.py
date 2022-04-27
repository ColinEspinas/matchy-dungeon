import pygame

from core.game import Game
from entities.grid import Grid
from entities.player import Player

game = Game({ 'title': 'Game', 'size': (1000, 600) }, 240)

game.addEntity('grid', Grid(game))

game.addEntity('player', Player(game))

# game.addEntity('player2', Player(game, {
#   'position': Vector2(game.screen.get_width() - 10, game.screen.get_height() / 2 - 50)
# }))

game.run()