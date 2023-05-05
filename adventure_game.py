import time
import random
villains = ["Lurid Lake dragon", "moss troll", "demon of candor"]
villain = random.choice(villains)
weapons = ["Mythic Flail", "Hephaestus Halberd", "Grenade from "
                                                 "Colonel Luxembourg"]
weapon = random.choice(weapons)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(villain):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, "
                "and has been terrorizing the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def field(item, villain):
    while True:
        response = input("Enter 1 to knock on the door.\n"
                         "Enter 2 to peer into the cave.\n"
                         "What would you like to do?\n"
                         "(Please enter 1 or 2).\n")
        if response == '1':
            print_pause("You are about to knock when the door opens and "
                        f"out steps the {villain}.")
            house(item, villain)
            break
        elif response == '2':
            print_pause("You peer cautiously into the cave.")
            cave(item, weapon)
            break
        else:
            print_pause("(Please enter 1 or 2).\n")


def house(item, villain):
    print_pause(f"Whoa! This is the {villain}'s house!")
    print_pause(f"The {villain} attacks you!")
    while True:
        response = input("Would you like to (1) fight or (2) run away?\n")
        if response == '1':
            fight(item, villain, weapon)
            break
        elif response == '2':
            run_away(item)
            break


def cave(item, weapon):
    if "weapon" not in item:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the {weapon}!")
        print_pause("You discard your silly old dagger and take "
                    "the legendary weapon with you.")
        item.append("weapon")
        print_pause("You walk back out into the field.\n")
        field(item, villain)
    else:
        print_pause("You've been here before and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out into the field.\n")
        field(item, villain)


def fight(item, villain, weapon):
    if "weapon" in item:
        print_pause(f"As the {villain} moves to attack, "
                    "you raise your new weapon.")
        print_pause(f"The {weapon} shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause(f"But the {villain} takes one look at the "
                    "legendary weapon and runs away!")
        print_pause(f"You have rid the town of the {villain}. "
                    "You are victorious!")
        print_pause("GAME OVER")
        play_again()
    elif "weapon" not in item:
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {villain}.")
        print_pause("You have been defeated!")
        print_pause("GAME OVER")
        play_again()


def run_away(item):
    print_pause("You run back to the field. Luckily, you don't "
                "seem to be followed.\n")
    field(item, villain)


def play_again():
    response = input("Would you like to play again? (y/n)\n").lower()
    if 'n' in response:
        print_pause("Thanks for playing! See you next time.")
    elif 'y' in response:
        print_pause("Excellent! Restarting the game.")
        play_game()
    else:
        play_again()


def play_game():
    item = []
    villain = random.choice(villains)
    weapon = random.choice(weapons)
    intro(villain)
    field(item, villain)


play_game()
