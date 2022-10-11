"""EX07!"""
__author__ = "730548206"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Takes original dictionary and convert it into the inverted dictionary."""
    if len(original_dict) > 0:
        i: int = 0
        inverted_dict: dict[str, str] = {}
        temporary_key_storage: list[str] = []
        temporary_value_storage: list[str] = []
        for keys in original_dict.keys():
            temporary_key_storage.append(keys)
        for values in original_dict.values():
            temporary_value_storage.append(values)
        while i < len(original_dict):
            print(temporary_key_storage[i], temporary_value_storage[i], i)
            new_dict: dict[str, int] = count(temporary_value_storage)
            if new_dict[temporary_value_storage[i]] > 1:
                raise KeyError
            else:
                inverted_dict[temporary_value_storage[i]] = temporary_key_storage[i]
            i += 1
        return inverted_dict
    else:
        return {}


def favorite_color(original_dataset: dict[str, str]) -> str:
    """Goes through a dictionary and return the most appeared color.If tied,first element of dict is returned."""
    colors_list: list[str] = []
    appearance_number: list[int] = []
    if len(original_dataset) > 0:
        for keys in original_dataset.values():
            colors_list.append(keys)
        value_and_its_appearance_number: dict[str, int] = count(colors_list)
        for numbers in value_and_its_appearance_number.values():
            appearance_number.append(int(numbers))
        maximum_appearance: int = max(appearance_number)
        i: int = 0
        tie_checker: int = 0
        while i < len(appearance_number):
            if maximum_appearance == appearance_number[i]:
                tie_checker += 1
            else:
                pass
            i += 1
        if tie_checker > 1:
            return colors_list[0]
        else:
            control_flow: bool = True
            counter: int = 0
            while counter < len(appearance_number) and control_flow is True:
                if appearance_number[counter] == maximum_appearance:
                    control_flow = False
                else:
                    counter += 1
            return colors_list[counter]
    else:
        print("The list is empty.")
        return ""


def count(org_list: list[str]) -> dict[str, int]:
    """Counts the number of appearance of an element in a list and returned dictionary."""
    new_dict: dict[str, int] = {}
    i: int = 0
    while i < len(org_list):
        if org_list[i] in new_dict:
            new_dict[org_list[i]] += 1
        else:
            new_dict[org_list[i]] = 1
        i += 1
    return new_dict
