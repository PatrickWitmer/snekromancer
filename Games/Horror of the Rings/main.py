# Import the Characters from character.py
from character import Mage, Rogue, Warrior

# Import the Envirment from environment.py
from environment import Environment


def game_loop():
    # Create characters
    mage = Mage("Kaeladil", 80, "Fireball")
    warrior = Warrior("Davic", 100, "Sword")
    rogue = Rogue("Boldoc", 70, "Stealth")

    # Create the Barrow-downs environment
    environment = Environment(
        "Barrow-downs", "A dark and eerie place filled with ancient tombs and spirits."
    )

    # Display the game introduction and initial state
    print(f"Welcome to the Horror of the Rings)")
    print(f"Your party consists of {mage.name}, {warrior.name} and {rogue.name}.")
    print(f"You are in the {environment.name}.")
    print(environment.description)

    # Game Loop
    while True:
        # Dislay the current state (e.g. health, environment, etc.)
        print(f"Your current location:", environment.name)

        # Ask for player input
        command = input("Enter a command (move, attack, use item, quit): ").lower()

        # Process commands
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "move":
            # Handle movement logic
            print("You move to another area.")
        elif command == "attack":
            # Handle attack logic
            print("You attack the enemy.")
        elif command == "use item":
            # Handle item usage logic
            print("You use an item.")
        else:
            print("Invalid command. Please try again.")
