"""EX08!"""
__author__ = "730548206"

from csv import DictReader

# Define your functions below

"""Some helpful utility functions for working with CSV files."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)
    # Read that file

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(original_dict: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` rows of data for each column."""
    if N > len(original_dict):
        return original_dict
    else:
        empty_dictionary: dict[str, list[str]] = {}
        for keys in original_dict.keys():
            empty_list: list[str] = []
            for i in range(0, N):
                empty_list.append(original_dict[keys][i])
            empty_dictionary[keys] = empty_list
        return empty_dictionary


def select(original_dictionary: dict[str, list[str]], original_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    empty_dictionary: dict[str, list[str]] = {}
    for column in original_list:
        empty_dictionary[column] = original_dictionary[column]
    return empty_dictionary


def concat(first_dict: dict[str, list[str]], second_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    empty_dict: dict[str, list[str]] = {}
    for keys in first_dict:
        empty_dict[keys] = first_dict[keys]
    for columns in second_dict:
        if columns in empty_dict.keys():
            for i in range(len(second_dict[columns])):
                empty_dict[columns].append(second_dict[columns][i])
        else:
            empty_dict[columns] = second_dict[columns]
    return empty_dict


def count(original_list: list[str]) -> dict[str, int]:
    """This function will produce a dict where each key is a unique value in the given list."""
    """And, each value associated is the _count_ of the number of times that value appeared in the input list."""
    empty_dict: dict[str, int] = {}
    for element in original_list:
        if element in empty_dict:
            empty_dict[element] += 1
        else:
            empty_dict[element] = 1
    return empty_dict
