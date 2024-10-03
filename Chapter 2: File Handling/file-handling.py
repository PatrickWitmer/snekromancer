player_stats = {
    "health": 100,
    "mana": 50,
    "level": 1,
}


def save_game():
    with open("game_save.text", "w") as file:
        for stat, value in player_stats.items():
            file.write(f"{stat}: {value}\n")
        print("Game saved!")


def load_game():
    global player_stats
    try:
        with open("game_save.text", "r") as file:
            for line in file:
                stat, value = line.split(":")
                player_stats[stat] = int(value)
        print("Game loaded!")
    except FileNotFoundError:
        print("No saved game found.")


# Test saving and loading
save_game()
load_game()
