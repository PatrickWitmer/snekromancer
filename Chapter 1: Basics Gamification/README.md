### Chapter One

# Basics Gamification

![Gandalf let's go on an adventure](../images/gandalf1.png)

## 1. Variables

Variables are containers for storing data values. In python, you don't need to declare the type of variable; Python figures it out for your when you assign a value.

```python
# Example
name = "Vlad" # A String variable
age = 150 # An integer variable
```

### Gamified Example:

You are a wizard who needs to gather magical ingredients. Each ingredient is a variable.

```python
# Let's collect magic ingredients
ingredient1 = "Dragon’s Scale"
ingredientAmount = 5 # Quantity of the ingredient

# Print them out as part of your spell
print("To cast the spell, you need:")
print(ingredient1, "and", ingredientAmount, "units of moon dust.")
```

## 2. Data Types

There are different data types in Python such as:

- **int**: Whole numbers
- **float**: Decimal numbers
- **str**: Strings (text)
- **bool**: Booleans (True or False)

```python
# Example
mana = 10 # Integar
pi = 3.14 # Float
message = "Welcome, adventurer!" # String
isMagic = True # Boolean
```

### Gamified Example:

You are a wizard’s shop, calculating the total cost of items. The items are strings, prices are floats, fand the decision to buy is a boolean.

```python
item = "Potion of Strength" # String
price = 6.66 # Float
buy = True # Boolean

print("You are buying, item")
print("It costs", price, "gold coins.")

didBuy = input("Do you want to buy it? (y/n)")

if didBuy == "y":
    print("You purchaced the item!")
else:
    print("You didn't buy the item.")
```

## 3. Conditionals (if-else)

Conditional statements allow you to make decisions in your code.

```python
mana = 20
if mana < 30:
    print("You are low on mana!")
else:
    print("DoTs we need more DoTs and you have the mana.")
```

### Gamified Example:

You're in battle! The game checks if your health is below a certain value to give your a warning.

```python
health = 18

if health < 30:
  print("Your health is critically low!")
else:
  print("Tis but a flesh wound, keep fighting!")
```

## 4. Loops (for, while)

Loops allow you repeat a block of code multiple times.

- **for:** Loops over a sequence (list, tuple, string, dictionary, etc.)
- **while:** Repeats as long as a condition is true.

```python
# Example

# For loop
for i in range(3):
    print("Loop iteration", i)

# While loop
mana = 5
while mana > 0:
  print("Casting spell")
  mana -= 1
```

### Gamified Example:

You are casting spells continually until you run out of mana.

```python
mana = 5
while mana > 0:
    print("Casting spell")
    mana -= 1

print("You are out of mana")
```
