
def play_game():
    print("\n================================")
    print(" MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    print("================================")

    # PLAYER INFORMATION
    player_name = input("What is your name, adventurer? ")

    energy = 5
    current_location = "Beach"
    inventory = []
    game_running = True
    game_over = False

    cave_path = None
    has_rest = False

    print(f"\nWelcome, {player_name}!")
    print("You are stranded on a mysterious island.")
    print("Your mission is to reach the Lighthouse and light its beacon.")
    print(f"Your starting energy is {energy}.")

    while game_running and not game_over:

        print("\n========== MYSTERY ISLAND ==========")
        print(f"Current location: {current_location}")
        print(f"Energy: {energy}")
        print("-----------------------------------")
        print("1. Explore the Beach")
        print("2. Travel to the Jungle")
        print("3. Explore the Jungle")
        print("4. Travel to the Cave")
        print("5. Explore the Cave")
        print("6. Rest in the Cave")
        print("7. Travel to the Old Bridge")
        print("8. Cross the Old Bridge")
        print("9. Light the Lighthouse")
        print("10. Check player status")
        print("11. Quit game")

        choice = input("Choose an option: ").strip()

        # 1. EXPLORE THE BEACH
        if choice == "1":

            if current_location != "Beach":
                print("\nYou are not currently at the Beach.")

            elif "rope" in inventory:
                print("\nYou have already collected the rope.")

            else:
                print("\nYou are exploring the Beach.")
                print("You discover a strong rope near the shore.")
                print("1. Pick up the rope")
                print("2. Leave the rope")

                beach_choice = input("What would you like to do? ").strip()

                if beach_choice == "1":
                    inventory.append("rope")
                    print("You picked up the rope!")

                elif beach_choice == "2":
                    print("You left the rope behind.")

                else:
                    print("Invalid choice. Please try again.")

        # 2. TRAVEL TO THE JUNGLE
        elif choice == "2":

            if current_location == "Jungle":
                print("\nYou are already in the Jungle.")

            elif current_location != "Beach":
                print("\nYou must be at the Beach to travel to the Jungle.")

            elif energy > 0:
                energy -= 1
                current_location = "Jungle"

                print("\nYou travelled from the Beach to the Jungle.")
                print("The forest is dark and mysterious.")
                print(f"Remaining energy: {energy}")

                if energy == 0:
                    print("\nYou have run out of energy!")
                    print("GAME OVER!")
                    game_over = True

            else:
                print("\nYou have no energy left.")

        # 3. EXPLORE THE JUNGLE
        elif choice == "3":

            if current_location != "Jungle":
                print("\nYou must travel to the Jungle before exploring it.")

            elif "lantern" in inventory:
                print("\nYou have already collected the lantern.")

            else:
                print("\nYou discover an old lantern beneath a tree.")
                print("1. Pick up the lantern")
                print("2. Leave the lantern")

                jungle_choice = input("What would you like to do? ").strip()

                if jungle_choice == "1":
                    inventory.append("lantern")
                    print("You picked up the lantern!")

                elif jungle_choice == "2":
                    print("You left the lantern behind.")

                else:
                    print("Invalid choice. Please try again.")

        # 4. TRAVEL TO THE CAVE
        elif choice == "4":

            if current_location == "Cave":
                print("\nYou are already in the Cave.")

            elif current_location != "Jungle":
                print("\nYou must be in the Jungle to travel to the Cave.")

            elif energy > 0:
                energy -= 1
                current_location = "Cave"

                print("\nYou travelled from the Jungle to the Cave.")
                print("The cave is cold, dark and mysterious.")
                print(f"Remaining energy: {energy}")

                if energy == 0:
                    print("\nYou have run out of energy!")
                    print("GAME OVER!")
                    game_over = True

            else:
                print("\nYou have no energy left.")

        # 5. EXPLORE THE CAVE
        elif choice == "5":

            if current_location != "Cave":
                print("\nYou must travel to the Cave before exploring it.")

            elif cave_path is not None:
                print("\nYou have already explored the Cave.")

                if cave_path == "stream":
                    print("You remember the ancient clue you discovered.")
                else:
                    print("You remember taking the rocky path.")

            else:
                print("\nTwo paths lie before you.")
                print("1. Take the underground stream (costs 1 energy)")
                print("2. Take the rocky path (costs no energy)")

                cave_choice = input("Which path will you choose? ").strip()

                if cave_choice == "1":

                    if energy > 0:
                        energy -= 1
                        cave_path = "stream"

                        print("\nYou followed the underground stream.")
                        print("You discovered an ancient clue on the cave wall!")
                        print("The clue reads:")
                        print("'The lighthouse needs light to guide the lost.'")
                        print(f"Remaining energy: {energy}")

                        if energy == 0:
                            print("\nYou have run out of energy!")
                            print("GAME OVER!")
                            game_over = True

                    else:
                        print("\nYou do not have enough energy.")

                elif cave_choice == "2":
                    cave_path = "rocky"

                    print("\nYou followed the rocky path.")
                    print("You found no useful items or clues.")
                    print("However, you saved your energy.")

                else:
                    print("Invalid choice. Please try again.")

        # 6. REST IN THE CAVE
        elif choice == "6":

            if current_location != "Cave":
                print("\nYou can only rest inside the Cave.")

            elif cave_path is None:
                print("\nExplore the Cave before deciding to rest.")

            elif has_rest:
                print("\nYou have already rested in the Cave.")

            elif energy >= 5:
                print("\nYour energy is already full.")

            else:
                energy += 1
                has_rest = True

                print("\nYou rested and recovered 1 energy point.")
                print(f"Your remaining energy is {energy}.")

        # 7. TRAVEL TO THE OLD BRIDGE
        elif choice == "7":

            if current_location == "Old Bridge":
                print("\nYou are already at the Old Bridge.")

            elif current_location != "Cave":
                print("\nYou must be in the Cave to travel to the Old Bridge.")

            elif energy > 0:
                energy -= 1
                current_location = "Old Bridge"

                print("\nYou have reached the Old Bridge.")
                print("A deep river flows beneath it.")
                print(f"Remaining energy: {energy}")

                if energy == 0:
                    print("\nYou have run out of energy!")
                    print("GAME OVER!")
                    game_over = True

            else:
                print("\nYou have no energy left.")

        # 8. CROSS THE OLD BRIDGE
        elif choice == "8":

            if current_location != "Old Bridge":
                print("\nYou must be at the Old Bridge to cross it.")

            elif "rope" not in inventory:
                print("\nYou cannot cross the bridge without a rope!")
                print("You should have collected the rope at the Beach.")

            elif energy <= 0:
                print("\nYou do not have enough energy to cross.")

            else:
                energy -= 1
                current_location = "Lighthouse"

                print("\nYou used your rope to cross the Old Bridge!")
                print("You have successfully reached the Lighthouse.")
                print(f"Remaining energy: {energy}")

                if energy == 0:
                    print("\nYou have run out of energy!")
                    print("GAME OVER!")
                    game_over = True

        # 9. LIGHT THE LIGHTHOUSE
        elif choice == "9":

            if current_location != "Lighthouse":
                print("\nYou must reach the Lighthouse first.")

            elif "lantern" not in inventory:
                print("\nYou cannot light the Lighthouse without a lantern!")
                print("You should have collected it in the Jungle.")

            else:
                print("\nYou raise your lantern and light the Lighthouse!")
                print("Its bright beam shines across the ocean.")
                print("A rescue ship spots the light!")
                print(f"\nCongratulations, {player_name}!")
                print("YOU HAVE WON THE GAME!")

                game_over = True

        # 10. CHECK PLAYER STATUS
        elif choice == "10":

            print("\n========== PLAYER STATUS ==========")
            print(f"Player: {player_name}")
            print(f"Location: {current_location}")
            print(f"Energy: {energy}")
            print(f"Inventory: {inventory}")
            print("===================================")

        # 11. QUIT GAME
        elif choice == "11":

            print(f"\nGoodbye, {player_name}!")
            print("Thanks for playing Mystery Island.")
            game_running = False

        # INVALID MENU INPUT
        else:
            print("\nInvalid option.")
            print("Please choose a number from 1 to 11.")

    return game_running



# MAIN GAME LOOP
def main():

    while True:

        play_again = play_game()

        if not play_again:
            break

        while True:
            replay = input(
                "\nWould you like to play again? (yes/no): "
            ).lower().strip()

            if replay in ("yes", "y"):
                break

            elif replay in ("no", "n"):
                print("\nThank you for playing Mystery Island!")
                print("See you on your next adventure.")
                return

            else:
                print("Invalid response. Please enter yes or no.")


# START GAME ONLY WHEN THIS FILE IS RUN DIRECTLY
if __name__ == "__main__":
    main()
