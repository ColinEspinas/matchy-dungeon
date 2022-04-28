import pygame

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
