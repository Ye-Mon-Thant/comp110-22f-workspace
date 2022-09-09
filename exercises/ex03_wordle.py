"""EX03 - Wordle"""
__author__ = "730548206"


def contains_char(first: str, second: str) -> bool:
    """Returns True only if the single character of the second string is found in first string."""
    assert len(second) == 1
    for i in range(0, len(first)):
        if second == first[i]:
            return True
        elif (second != first[i]) and (i == len(first) - 1):
            return False
        else:
            pass


def emojified(guess: str, secret: str) -> str:
    """Use contains_char function by calling it to test for yellow or white box codification."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    for i in range(0,len(guess)):
        if guess[i] == secret[i]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
    print(emoji_string)
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Given an integer “expected length” of a guess as a parameter, it will prompt the user for a guess until the length requirment is fulfilled."""
    input_word: str = str(input(f"Enter a {str(expected_length)} character word: "))
    while len(input_word) != expected_length:
        input_word = str(input(f"That wasn't {str(expected_length)} chars! Try again: "))
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET_WORD: str = "codes"
    turns: int = 1
    while turns < 7:
        print(f"=== Turn {str(turns)}/6 ===")
        result: str = emojified(input_guess(len(SECRET_WORD)), SECRET_WORD)
        number_of_green_boxes: int = 0
        for i in result:
            if i == GREEN_BOX:
                number_of_green_boxes += 1
            else:
                pass
        if number_of_green_boxes == len(SECRET_WORD):
            print(f"You won in {str(turns)}/6 turns!")
            quit()
        elif turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
            quit()
        else:
            turns += 1
            pass



WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if __name__ == "__main__":
    main()
