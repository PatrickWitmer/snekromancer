### Chapter Four

# Inheritance

![Frodo inherits the ring from Bilbo.](../images/bilbo.gif)

> With python we can inherit the ring of power.

## 11. Inheritance

Inheritance allows a new class to inherit properties and methods from an existing class. This helps in code reuse and establishing a hierarchy.

```python
# Example
class Character:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def attack(self):
    print(f"{self.name} attacks!")

# Inheriting from Character
class Warrior(Character):
  def __init__(self, name, health, weapon):
    super().__init__(name, health)
    self.weapon = weapon

    def attack(self):
      print(f"{self.name} attacks with {self.weapon}!")

# Creating a Warrior
hero = Warrior("Frodo", 100, "sword")
hero.attack()
```

### Gamified Example:

Create different character classes, like Mage and Warrior, to showcase inheritance and specialization.

```python
# Base Character class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with a basic strike!")

# Mage subclass inheriting from Character
class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)  # Call the __init__ of the parent class
        self.spell = spell

    def cast_spell(self):
        print(f"{self.name} casts {self.spell}!")

# Warrior subclass inheriting from Character
class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} swings their {self.weapon}!")

# Create a Mage instance
mage = Mage("Gandalf", 80, "Fireball")
mage.attack()  # Inherited from Character
mage.cast_spell()  # Mage specific

# Create a Warrior instance
warrior = Warrior("Aragorn", 100, "Sword")
warrior.attack()  # Overridden attack method in Warrior

```
