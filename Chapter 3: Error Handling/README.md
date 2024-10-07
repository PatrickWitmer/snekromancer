### Chapter Three

# Error Handling

![Fool of a Took.](../images/gandalf3.gif)

> Because we are sometimes a fool of a Took, let's take a look at error handling in python.

## 10. Error Handling

Error handling allow you to manage exceptions gracefully without crashing the program. You can use try and except blocks to catch errors.

```python
# Example
try:
  value = int(input("Enter a number: "))
  print(f"You entered: {value}")
except ValueError:
  print("That’s not a valid number.")
```

### Gamified Example:

Let’s add a way to safely load players stats, handling cases where the file might not exist.

```python
def safe_load_game():
  try:
    with open("game_save.text", "r") as file:
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
```
