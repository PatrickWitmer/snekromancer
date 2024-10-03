### Chapter One

# Basics Gamification

![Gandalf let's go on an adventure](../images/gandalf1.webp)

## 1. Variables

Variables are containers for storing data values. In python, you don't need to declare the type of variable; Python figures it out for your when you assign a value.

```python
# Example
name = "Vlad" # A String variable
age = 150 # An integer variable
```

### Gamified Example:

You are a wizard who needs to gather magical ingredients. Each ingredient is a variable.

```python
# Let's collect magic ingredients
ingredient1 = "Dragon’s Scale"
ingredientAmount = 5 # Quantity of the ingredient

# Print them out as part of your spell
print("To cast the spell, you need:")
print(ingredient1, "and", ingredientAmount, "units of moon dust.")
```

## 2. Data Types

There are different data types in Python such as:

- **int**: Whole numbers
- **float**: Decimal numbers
- **str**: Strings (text)
- **bool**: Booleans (True or False)

```python
# Example
mana = 10 # Integar
pi = 3.14 # Float
message = "Welcome, adventurer!" # String
isMagic = True # Boolean
```

### Gamified Example:

You are a wizard’s shop, calculating the total cost of items. The items are strings, prices are floats, fand the decision to buy is a boolean.

```python
item = "Potion of Strength" # String
price = 6.66 # Float
buy = True # Boolean

print("You are buying, item")
print("It costs", price, "gold coins.")

didBuy = input("Do you want to buy it? (y/n)")

if didBuy == "y":
    print("You purchaced the item!")
else:
    print("You didn't buy the item.")
```

## 3. Conditionals (if-else)

Conditional statements allow you to make decisions in your code.

```python
mana = 20
if mana < 30:
    print("You are low on mana!")
else:
    print("DoTs we need more DoTs and you have the mana.")
```

### Gamified Example:

You're in battle! The game checks if your health is below a certain value to give your a warning.

```python
health = 18

if health < 30:
  print("Your health is critically low!")
else:
  print("Tis but a flesh wound, keep fighting!")
```

## 4. Loops (for, while)

Loops allow you repeat a block of code multiple times.

- **for:** Loops over a sequence (list, tuple, string, dictionary, etc.)
- **while:** Repeats as long as a condition is true.

```python
# Example

# For loop
for i in range(3):
    print("Loop iteration", i)

# While loop
mana = 5
while mana > 0:
  print("Casting spell")
  mana -= 1
```

### Gamified Example:

You are casting spells continually until you run out of mana.

```python
mana = 5
while mana > 0:
    print("Casting spell")
    mana -= 1

print("You are out of mana")
```

## 5. Functions

Functions allow you to organize your code into reusable blocks.

```python
# Example
def greet_player():
  print("Welcome, brave adventurer!")

greetPlayer() # Call the function
```

### Gamified Example:

You are creating a function to calculate damage during a battle.

```python
def calculate_damage(strength, weapon_power):
  return strength * weapon_power

strength = 10
weapon_power = 3

damage = calculate_damage(strength, weapon_power)

print("You dealt", damage, "damage to the enemy.")
```

## 6. Lists

Lists are used to store multiple items in a single variable.

```python
# Example

inventory = ["sword", "shield", "potion", "spellbook"]
```

### Gamified Example:

You are managing your inventory in a game.

```python
inventory = ["Magic Wand", "Healing Potion", "Ancient Key"]

print("Current Inventory: ", inventory)

print("You have picked up a new item!")

inventory.append("Scroll of Fire")

print("Updated Inventory: ", inventory)
```

## 7. Dictionaries

Dicitionaries store key-value pairs.

```python
# Example
player_stats = {
    "health": 100,
    "mana": 50,
    "level": 2,
}
```

### Gamified Example:

You are keeping track of your character’s stats in a game.

```python
player_stats = {
    "health": 100,
    "mana": 75,
    "level": 3,
}

print("Player stats:")
for stat, value in player_stats.items():
    print(f"{stat}: {value}")

# Level up the player
player_stats["health"] += player_stats["health"] * 20 / 100
player_stats["mana"] += player_stats["mana"] * 50 / 100
player_stats["level"] += 1
print("\nAfter level up:", player_stats)
```

## 8. Classes

Classes are blueprints for creating objects (instances of the class).

```python
# Example
class Character:
    def __init__(self, name, health, mana, level):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    def attack(self):
      print(f"{self.name} attacks!")

# Create a character
hero = Character("Gandalf", 10000, 15000000, 100)
hero.attack()
```

### Gamified Example:

Create a class to reperesent a monster in a text-based game.

```python
class Monster:
    def __init__(self, name, health):
      self.name = name
      self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health left: {self.health}")

# Create a monster
goblin = Monster("Goblin", 100)
goblin.take_damage(50)
```
