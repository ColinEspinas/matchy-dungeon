from enum import Enum
import random

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

cellTypeWeight = {
  CellType.EMPTY: 20, 
  CellType.ATTACK: 20, 
  CellType.DEFENSE: 14, 
  CellType.GOLD: 10,
  CellType.PIKES: 20, 
  CellType.BASH: 16
}

def getRandomCellType():
  return random.choices(
    list(cellTypeWeight.keys()), 
    weights=list(cellTypeWeight.values()), 
    k=1
  )[0]