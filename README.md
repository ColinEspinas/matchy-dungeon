# Matchy Dungeon

A match-3/roguelike game where you fight infinite amount of monsters.

## Dependencies

| Name   | Version |
|--------|---------|
| pygame | 2.1.2   |

## About

### Player
The player has health points that can be shielded.

### Dungeon
The infinite dungeon is composed of floors. When you kill all the monsters of a floor you will get access to a shop.

The game gets harder as you progress through floors.

### Leveling
When killing an enemy you will get XP. Once per level you will get to increase a stat.

### Shops
In the shop you will get the choice to trade items for you acquired gold.

### Cell types
| Name    | Type          | Effect                                                      |
|---------|---------------|-------------------------------------------------------------|
| Attack  | Player Attack | Attacks the enemy monster for the number of connected tiles |
| Defense | Bonus         | Adds 1 to player shields                                    |
| Bash    | Enemy Attack  | Damage the player for the number of connected tiles  |
| Pikes   | Enemy Attack  | When walking on it damages the player for 1HP        |
| Gold    | Consumable    | Adds 1 gold to player's purse                        |

## Resources

Thanks https://phosphoricons.com/ for the sprite icons.