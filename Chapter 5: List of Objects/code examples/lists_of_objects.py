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
