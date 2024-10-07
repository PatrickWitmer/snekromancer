### Chapter Five

# Lists of Objects

![and my axe.](../images/gimli.webp)

> and my axe...and my sword...and my bow...and my second breakfast.

## 12. Lists of Objects

You can create a list that store instances of classes, allowing oyu to manage multiple objects easily.

```python
# Example
characters = []
characters.append(Character("Hero", 100 ))
characters.append(Mage("Sorcerer", 80, "Lightning"))

for character in characters:
  print(character.name, "has", character.health, "health.")
```

### Gamified Example:

Manage a party of adventurers, each with their own stats and abilities.

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# Mage subclass inheriting from Character
class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)
        self.spell = spell


# Warrior subclass inheriting from Character
class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon


# Adventurer Party
party = []
party.append(Warrior("Boromir", 110, "Shield"))
party.append(Mage("Elrond", 200, "Healing Light"))

print("Your adventurer party:")
for member in party:
    if isinstance(member, Warrior):
        print(f"{member.name} - Health: {member.health}, Weapon: {member.weapon}")
    elif isinstance(member, Mage):
        print(f"{member.name} - Health: {member.health}, Spell: {member.spell}")
```
