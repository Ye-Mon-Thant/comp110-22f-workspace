"""Example of looping through all characters in a string."""

user_string: str = input("give me a string! ")

i: int = 0

while i < len(user_string):
    print(user_string[i])
    i += 1

print("Done!")