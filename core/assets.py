import pygame

class Assets:
  def __init__(self) -> None:
    self.images = {
      # Icons
      'sword': pygame.image.load('assets/sprites/sword.png').convert_alpha(),
      'shield': pygame.image.load('assets/sprites/shield.png').convert_alpha(),
      'shield-filled': pygame.image.load('assets/sprites/shield-filled.png').convert_alpha(),
      'coin': pygame.image.load('assets/sprites/coin.png').convert_alpha(),
      'coin-filled': pygame.image.load('assets/sprites/coin-filled.png').convert_alpha(),
      'fist': pygame.image.load('assets/sprites/fist.png').convert_alpha(),
      'pike': pygame.image.load('assets/sprites/pike.png').convert_alpha(),
      'skull': pygame.image.load('assets/sprites/skull.png').convert_alpha(),
      'heart': pygame.image.load('assets/sprites/heart.png').convert_alpha(),

      # Monsters
    }
    self.fonts = {
      'regular': pygame.font.Font('assets/fonts/alagard.ttf', 30),
      'big-regular': pygame.font.Font('assets/fonts/alagard.ttf', 50),
    }