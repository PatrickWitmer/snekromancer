### Chapter Two

# File Handling

![Gandalf has no memory of this place.](../images/gandalf2.webp)

> Like Gandalf we have no way to store our data in a file. So let's learn the magic of files so we don't get lost in the dark.

## 9. File Handling

File handling in python allows you to read and write data to files. This is useful for saving game states, high scores, or player progress.

```python
# Example: Writing to a file
with open("game_save.text", "w") as file:
  file.write("Player Health: 100\n")
  file.write("Player Mana: 50\n")

# Example: Reading from a file
with open("game_save.text", "r") as file:
  data = file.read()
  print(data)
```

### Gamified Example:

We will add functionality to save and load the player’s progress in our game.

```python
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
```
