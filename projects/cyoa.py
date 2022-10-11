"""Ex06."""
__author__ = 730548206
from random import randint


points: int = 0
player: str = ""
RED_EMOJI_BOX: str = "\U0001F7E5"
GREEN_BOX: str = "\U0001F7E9"


def main() -> None:
    """The main function definition."""
    greet()
    controller2: bool = True
    while controller2 is True:
        global points
        print(f"Your total score is {points}")
        user_input: int = int(input("Press 1 to play coin flipping game.\n"
                                    "Press 2 to play number guessing game.\n"
                                    "Press 3 to end the program."))
        if user_input == 1:
            procedure1()
        elif user_input == 2:
            points = procedure2(points)
        elif user_input == 3:
            print(f"Bye Bye, {player}! Have a nice day.")
            quit()
        else:
            print("Please enter either 1 or 2.")


def greet() -> None:
    """Greets the player and assign the player's name to the global player function."""
    print("Welcome to the adventurous game!")
    global player
    player = str(input("What's your name?\nEnter here: "))
    return None


def procedure1() -> None:
    """Coin flipping game."""
    possibilities: list[str] = ["Head", "Tail"]
    win_streak: int = 0
    controller: bool = True
    while controller is True:
        input1: int = int(input(f"{player}, Press 1 to play the coin flipping game or 2 to stop it: "))
        controller1: bool = True
        if input1 == 1:
            while controller1 is True:
                input2: int = int(input("The coin has been tossed up into the air, and landed onto my hand....\n"
                                        "Which side is facing downwards?\nPress 1 for head and 2 for tail.\n"
                                        "Enter here: "))
                side_determinator: str = possibilities[randint(0, 1)]
                if input2 == 1 or 2:
                    if possibilities[input2 - 1] == side_determinator:
                        global GREEN_BOX
                        print(f"{GREEN_BOX}{GREEN_BOX}")
                        global points
                        points += 1
                        win_streak += 1
                        continue
                    else:
                        global RED_EMOJI_BOX
                        print(f"{RED_EMOJI_BOX}{RED_EMOJI_BOX}\n"
                              f"Sorry! The side facing down was {side_determinator}.\nYour win streak is {win_streak},"
                              "and you will be returned back to the secondary page!")
                        win_streak = 0
                        controller1 = False
                else:
                    print("Please enter either 1 or 2.")
        elif input1 == 2:
            return None
        else:
            print("Please enter either 1 or 2.")


def procedure2(original_score: int) -> int:
    """The number guessing game!!"""
    tries: int = 0
    controller3: bool = True
    while controller3 is True:
        user_input3: int = int(input(f"{player}, Press 1 to play the game or 2 to quit.\nEnter here: "))
        if user_input3 == 1:
            user_input4: int = int(input("Choose the maximum number so that a random number will be chosen in range of"
                                         " 1 and this number: "))
            controller4: bool = True
            while controller4 is True:
                if user_input4 > 1:
                    random_chosen_integer: int = randint(1, user_input4)
                    user_chosen_integer: int = int(input("Press 0 to stop or choose a number of your choice: "))
                    if user_chosen_integer == random_chosen_integer:
                        print(f"Congrats! You have correctly guessed the random number in {tries + 1} tries.")
                        controller4 = False
                        original_score += 1
                    elif user_chosen_integer == 0:
                        controller4 = False
                    else:
                        print("Incorrect! Try again!")
                        tries += 1
                        pass
                else:
                    print("Please enter positive numbers that are greater than 1 only!")
                    controller4 = False
        elif user_input3 == 2:
            controller3 = False
        else: 
            print("Please enter either 1 or 2.")
    return original_score
            

if __name__ == "__main__":
    main()
