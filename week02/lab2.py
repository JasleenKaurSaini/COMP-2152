import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
diceRoll = [1, 2, 3, 4, 5, 6]

input("ROLL YOUR DICE")

weaponRoll = random.choice(diceRoll)
weaponChoice = weapons[weaponRoll - 1]

print("You rolled the number: " + str(weaponRoll))
print("The weapon is: " + weaponChoice)

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if weaponChoice != "Fist":
    print("Thank goodness you didn't roll the Fist...")

combatInput = input("Enter your combat strength: ")

if combatInput.isdigit():
    combat_strength = int(combatInput)
    print(f"Your combat strength is: {combat_strength}")
else:
    print("Error: Invalid integer.")
    exit()
# LAB 2
# LAB 2
