def safe_load_game():
    try:
        with open("game_save.text", "r") as file:
            for line in file:
                stat, value = line.strip().split(":")
                player_stats[stat] = int(value)
                print("Game loaded successfully!")
    except FileNotFoundError:
        print("No saved game found, starting fresh.")
    except ValueError:
        print("Error in saved data, resetting to default stats.")
        player_stats = {
            "health": 100,
            "mana": 50,
            "level": 1,
        }


# Test the safe load function
safe_load_game()
