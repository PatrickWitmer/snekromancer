# Building Rubick’s Spellbook

# Create a spellbook with a Rubick’s spells (as python functions).

# Rubick’s spells are:

# 1. Telekinesis
# 2. Fade Bolt
# 3. Arcane Supremacy
# 4. Spell Steal

import random

# Rubick’s mana pool
rubick_mana = 100

# Experience and level up system
rubick_exp = 0
rubick_level = 1


# Spellbook (spells are functions)
def black_hole():
    global rubick_mana
    if rubick_mana >= 15:
        rubick_mana -= 15
        print("⚫️ Rubick casts black hole! How many did we catch?")
        gain_experience(30)
    else:
        print("Not enough mana to cast blackhole")


def echo_slam():
    global rubick_mana
    if rubick_mana >= 10:
        rubick_mana -= 10
        print("🪨 Rubick casts Echo Slam! Damage for 10 HP.")
        gain_experience(30)
    else:
        print("Not enough mana to cast Echo Slam")


def ravage():
    global rubick_mana
    if rubick_mana >= 20:
        rubick_mana -= 20
        print("🪨 Rubick casts Ravage! Damage for 20 HP.")
        gain_experience(30)
    else:
        print("Not enough mana to cast Ravage")


enemy_spellbook = {"black_hole": black_hole, "echo_slam": echo_slam, "ravage": ravage}

rubick_spell_inventory = []


# Function to steal spells
def steal_spell(spell_name):
    if spell_name in enemy_spellbook:
        print(f"🔮 Rubick steals {spell_name}!")
        rubick_spell_inventory.append(enemy_spellbook[spell_name])
    else:
        print("Spell {spell_name} not found in enemy spellbook")


# Cast a spell that is stolen
def cast_stolen_spell(spell_index):
    if rubick_spell_inventory:
        rubick_spell_inventory[spell_index]()
    else:
        print("Rubick hasn’t stolen any spells yet")


# Gain experience points for casting spells
def gain_experience(xp_gained):
    global rubick_exp, rubick_level
    rubick_exp += xp_gained
    print(f"Rubick gains {xp_gained} experience points.")
    if rubick_exp >= rubick_level * 100:
        rubick_level += 1
        print(f"🧙‍♂️ Rubick levels up! He is now level {rubick_level}")


# Check rubick’s mana
def check_mana():
    print(f"Rubick has {rubick_mana} mana left")


# Example gameplay
steal_spell("black_hole")
cast_stolen_spell(0)  # cast black hole
check_mana()
steal_spell("echo_slam")
cast_stolen_spell(1)  # cast echo slam
check_mana()
steal_spell("ravage")
cast_stolen_spell(2)  # cast ravage
check_mana()
steal_spell("black_hole")
cast_stolen_spell(0)  # cast black hole
check_mana()
steal_spell("echo_slam")
cast_stolen_spell(1)  # cast echo slam
check_mana()
steal_spell("ravage")
cast_stolen_spell(2)  # cast ravage
check_mana()
cast_stolen_spell(1)  # cast echo slam
check_mana()
steal_spell("ravage")
cast_stolen_spell(2)  # cast ravage
check_mana()
