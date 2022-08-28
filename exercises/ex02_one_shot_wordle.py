"""EX02 - One-short Wordle."""
__author__ = "730548206"


SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
counter: int = 0
resulting_emoji: str = ""
s: int = 0 # a variable that measures the number of times an element in the user guess (that matched one of the elements of SECRET_WORD) has appeared as emoji box

user_guess: str = input("What is your 6-letter guess? ")

while len(user_guess) != 6:
    user_guess = input("That was not 6 letters! Try again: ")

while counter < len(user_guess):
    if user_guess[counter] == SECRET_WORD[counter]:
        resulting_emoji = resulting_emoji + GREEN_BOX + " "

    else:
        s = 0
        for i in range(0, len(user_guess)):
            if user_guess[counter] == SECRET_WORD[i]:
                if s < 1:
                    resulting_emoji = resulting_emoji + YELLOW_BOX + " "
                    s += 1
                else:
                    pass
            elif (user_guess[counter] != SECRET_WORD[i]) and (i == len(user_guess) - 1) and (s == 0):
                resulting_emoji = resulting_emoji + WHITE_BOX + " "
            else:
                pass
    
    counter += 1


if user_guess == SECRET_WORD:
    print(resulting_emoji)
    print("Woo! You got it!")
else:
    print(resulting_emoji)
    print("Not quite. Play again soon!")