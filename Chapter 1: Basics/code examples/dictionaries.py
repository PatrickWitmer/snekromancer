player_stats = {
    "health": 100,
    "mana": 75,
    "level": 3,
}

print("Player stats:")
for stat, value in player_stats.items():
    print(f"{stat}: {value}")

# Level up the player
player_stats["health"] += player_stats["health"] * 20 / 100
player_stats["mana"] += player_stats["mana"] * 50 / 100
player_stats["level"] += 1
print("\nAfter level up:", player_stats)
