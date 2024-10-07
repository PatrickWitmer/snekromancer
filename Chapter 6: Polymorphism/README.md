### Chapter Six

# Polymorphism

![eyes of wonder](../images/gollum.webp)

> Wonder is the eye of the wise.

## 13. Polymorphism

Polymorphism allows objects of different types to be treated as if they are the same type. This is particularly useful in scenarios where different classes have methods with the same name., and you want to call those methods on objects without worrying about the object’s specific class.

Example: Let’s extend our previous RPG example with polymorphism. Suppose both `Mage` and `Warrior` have a `attack()` method, but each class implements it differently.

```python
# Base Character class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        pass # Define in subclasses

# Mage subclass with a specific attack method
class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)
        self.spell = spell

    def attack(self):
        print(f"{self.name} casts {self.spell}!")

# Warrior subclass with a specific attack method
class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} swings their {self.weapon}!")

# Adventurer Party
party = [
  Warrior("Boromir", 110, "Shield"),
  Mage("Elrond", 200, "Fireball"),
  Warrior("Aragorn", 100, "Sword"),
]

print("Your adventurer party attacks!")
for member in party:
    member.attack()
```
