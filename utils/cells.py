from enum import Enum

class CellType(Enum):
  EMPTY = 0
  ATTACK = 1
  DEFENSE = 2
  GOLD = 3
  PIKES = 4
  BASH = 5

cellTypes = [
  CellType.EMPTY, 
  CellType.ATTACK, 
  CellType.DEFENSE, 
  CellType.GOLD, 
  CellType.PIKES, 
  CellType.BASH
]