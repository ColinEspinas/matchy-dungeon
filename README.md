# Matchy Dungeon

A match-3/roguelike game where you fight infinite amount of monsters.

## Dependencies

| Name   | Version |
|--------|---------|
| pygame | 2.1.2   |

## About

### Player
The player has health points that can be shielded.
Player can generate a combo by chaining cells of the same type together:
- 3 cells for 1
- 5 cells for 2
- 10 cells for 3

Even enemy cells give combo. The only exceptions are pikes and empty cells.
The combo will be reset if you don't chain at least 3 cells in 3 seconds.

### Dungeon
The infinite dungeon is composed of floors. When you kill all the monsters of a floor you will get access to a shop before progressing to the next floor.

The game gets harder as you progress through floors.

Upon reaching a new floor combo is reset.

### Leveling
When killing an enemy you will get XP. Once per level you will get to increase a stat.

### Shops
In the shop you will get the choice to trade items for you acquired gold.

### Cell types
| Name    | Type          | Effect                                                      |
|---------|---------------|-------------------------------------------------------------|
| Attack  | Player Attack | Attacks the enemy monster for the number of connected tiles multiplied by the current combo |
| Defense | Bonus         | Adds 1 to player shields                                    |
| Bash    | Enemy Attack  | Damage the player for the number of connected tiles         |
| Pikes   | Enemy Attack  | When walking on it damages the player for 1HP               |
| Gold    | Consumable    | Adds 1 gold to player's purse                               |

## Current state

What is missing:
- Leveling system
- Shops
- Coins are useless as there is no shop in game yet (you can still use them for combo).

## Resources

Thanks https://phosphoricons.com/ for the sprite icons.