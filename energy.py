# Starting energy
energy = 5

print(f"Starting energy: {energy}")

# Reduce energy by 1
energy -= 1

print(f"Remaining energy: {energy}")

# Check if energy is finished
if energy == 0:
    print("You have no energy left.")
else:
    print("You still have energy to continue.")