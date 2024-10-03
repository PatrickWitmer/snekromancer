def calculate_damage(strength, weapon_power):
    return strength * weapon_power


strength = 10
weapon_power = 3

damage = calculate_damage(strength, weapon_power)

print("You dealt", damage, "damage to the enemy.")
