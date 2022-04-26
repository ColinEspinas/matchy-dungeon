import pygame

from core.game import Game
from entities.player import Player
from entities.ball import Ball
from pygame.math import Vector2

game = Game({ 'title': 'Game', 'size': (600, 400) })

game.addEntity('ball', Ball(game, {
  'position': Vector2(game.screen.get_width() / 2 - 3, game.screen.get_height() / 2 - 3)
}))

game.addEntity('player1', Player(game, {
  'position': Vector2(0, game.windowOptions['size'][1] / 2 - 50),
  'keys': {
    'up': pygame.K_z,
    'down': pygame.K_s
  }
}))

game.addEntity('player2', Player(game, {
  'position': Vector2(game.screen.get_width() - 10, game.screen.get_height() / 2 - 50)
}))

game.run()