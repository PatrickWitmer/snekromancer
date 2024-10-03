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
