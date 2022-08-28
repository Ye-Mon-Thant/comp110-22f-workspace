"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730548206"


instances: int = 0
chosen_word: str = input("Enter a 5-character word: ")
if len(chosen_word) == 5:
    chosen_character: str = input("Enter a single character: ")
    if len(chosen_character) == 1:
        print(f"Searching for {chosen_character} in {chosen_word}")
        for i in range(0, len(chosen_word)):
            if chosen_character == chosen_word[i]:
                instances += 1
                print(f"{chosen_character} found at index {i}")
                if i == 4:
                    if instances == 1:
                        print(f"{instances} instance of {chosen_character} found in {chosen_word}")
                    elif instances > 1:
                        print(f"{instances} instances of {chosen_character} found in {chosen_word}")
                    else:
                        print(f"No instances of {chosen_character} found in {chosen_word}")
            else:
                if i == 4:
                    if instances == 1:
                        print(f"{instances} instance of {chosen_character} found in {chosen_word}")
                    elif instances > 1:
                        print(f"{instances} instances of {chosen_character} found in {chosen_word}")
                    else:
                        print(f"No instances of {chosen_character} found in {chosen_word}")
                else:
                    pass
    else:
        print("Error: Character must be a single character.")
        exit()

else:
    print("Error: Word must contain 5 characters")
    exit()
