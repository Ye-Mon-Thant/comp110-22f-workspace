"""Ex04 - Utils."""
__author__ = "730548206"


def all(a: list[int], b: int) -> bool:
    """Checking whether b is the same as all of the elements in list a."""
    i = 0
    counter = 0
    if len(a) == 0:
        return False
    else:
        while i < len(a):
            if a[i] == b:
                counter += 1
            else:
                pass
            i += 1
        if counter == len(a):
            return True
        else:
            return False


def max(input: list[int]) -> int:
    """This should return the largest element in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        result: int = 0
        while i < len(input):
            if len(input) > 1:
                if i == 0:
                    if input[i] > input[i + 1]:
                        result = input[i]
                    elif input[i] < input[i + 1]:
                        result = input[i + 1]
                    elif input[i] == input[i + 1]:
                        result = input[i]
                    else:
                        print("Something went wrong!")
                    i += 1
                    continue
                elif i != 0:
                    if i == 1:
                        i += 1
                        continue
                    else:
                        if result > input[i]:
                            pass
                        elif result < input[i]:
                            result = input[i]
                            pass
                        else:
                            pass
                        i += 1
                        print(i, len(input), result)
                        continue
                else:
                    print("Something went wrong!")
            else:
                result = input[i]
                i += 1
    return result


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(input1) == len(input2):
        i: int = 0
        truth_counter: int = 0
        while i < len(input1):
            if input1[i] == input2[i]:
                truth_counter += 1
            else:
                pass
            i += 1
        if truth_counter == len(input1):
            return True
        else:
            return False
    else:
        print("The number of elements in list is different and therefore can't be True.")
        return False
