"""An example of a while loop statement."""

counter: int = 0
maximum: int = int(input("Count up to but not including what?"))
while counter < maximum:
    print(counter)
    print("The square of", str(counter),"is", str(counter ** 2) + ".")
    counter += 1

print("Done!")