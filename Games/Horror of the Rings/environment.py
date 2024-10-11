class Environment:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Create the Barrow-downs environment
barrow_downs = Environment(
    "Barrow-downs",
    "Barrow-downs is a dark and eerie place. The air is thick with the smell of death and decay. The walls are made of black stone, and the floors are covered in cobwebs. The only light comes from the flickering torches that hang from the ceiling, casting eerie shadows on the walls.",
)

# Display the environment details
print(f"You are in the {barrow_downs.name}.")
print(barrow_downs.description)
