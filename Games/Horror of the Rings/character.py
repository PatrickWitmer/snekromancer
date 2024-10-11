class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")


class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} swings their {self.weapon}!")


class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)
        self.spell = spell

    def cast_spell(self):
        print(f"{self.name} casts {self.spell}")


class Rogue(Character):
    def __init__(self, name, health, special_ability):
        super().__init__(name, health)
        self.special_ability = special_ability

    def special_ability(self):
        print(f"{self.name} performs a {self.special_ability}")
