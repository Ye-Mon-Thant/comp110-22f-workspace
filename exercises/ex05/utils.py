"""Ex05."""
__author__ = "730548206"


def only_evens(input0: list[int]) -> list[int]:
    """Only Even numbers result from original list."""
    result: list[int] = []
    if len(input0) != 0:
        for i in input0:
            if i % 2 == 0:
                result.append(i)
            else:
                pass
        return result
    else:
        return result


def sub(input3: list[int], start_index: int, end_index: int) -> list[int]:
    """Sub."""
    result_sublist: list[int] = []
    if len(input3) == 0 or start_index > len(input3) or end_index <= 0:
        return result_sublist
    elif start_index >= 0 and end_index < len(input3):
        for i in range(start_index, end_index):
            result_sublist.append(input3[i])
        return result_sublist
    elif start_index < 0 and end_index < len(input3):
        for s in range(0, end_index):
            result_sublist.append(input3[s])
        return result_sublist
    elif end_index > len(input3):
        if start_index >= 0:
            for counter1 in range(start_index, len(input3)):
                result_sublist.append(input3[counter1])
            return result_sublist
        elif start_index < 0:
            for counter2 in range(0, end_index):
                result_sublist.append(input3[counter2])
            return result_sublist
    else:
        print("The code went through here, which is unexpected.")
        

def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Concat two lists."""
    result_list: list[int] = []
    for i in input1:
        result_list.append(i)
    for s in input2:
        result_list.append(s)
    return result_list
