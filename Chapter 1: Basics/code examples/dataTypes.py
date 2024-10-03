item = "Potion of Strength"  # String
price = 6.66  # Float
buy = True  # Boolean

print("You are buying", item)
print("It costs", price, "gold coins.")

didBuy = input("Do you want to buy it? (y/n)")

if didBuy == "y":
    print("You purchaced the item!")
else:
    print("You didn't buy the item.")
