"""EX03 - Wordle."""
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
    return False


def emojified(guess: str, secret: str) -> str:
    """Use contains_char function by calling it to test for yellow or white box codification."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    counter: int = 0
    while counter <= (len(guess) - 1):
        if guess[counter] == secret[counter]:
            emoji_string += GREEN_BOX
            counter += 1
            continue
        elif contains_char(secret, guess[counter]) is True:
            emoji_string += YELLOW_BOX
            counter += 1
            continue
        else:
            emoji_string += WHITE_BOX
            counter += 1
            continue
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
    turns: int = 0
    while turns < 6:
        print(f"=== Turn {str(turns + 1)}/6 ===")
        inputt: str = input_guess(len(SECRET_WORD))
        result: str = emojified(inputt, SECRET_WORD)
        print(result)
        if inputt == SECRET_WORD:
            print(f"You won in {str(turns + 1)}/6 turns!")
            turns = 6
        elif turns >= 5:
            print("X/6 - Sorry, try again tomorrow!")
            turns += 1
        else:
            turns += 1


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if __name__ == "__main__":
    main()
