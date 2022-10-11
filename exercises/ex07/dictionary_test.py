"""Test Unit for EX07."""
__author__ = "730548206"

import pytest
from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_key_error():
    """Check whether it raises KeyError when the inverted keys are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty_list():
    """Test invert function with empty list."""
    empty_list: dict[str, str] = {}
    assert invert(empty_list) == {}


def test_invert_normal_list():
    """Test invert function with normal list."""
    normal_list: dict[str, str] = {'1': 'apple', '2': 'banana', '3': 'mango'}
    assert invert(normal_list) == {'apple': '1', 'banana': '2', 'mango': '3'}


def test_favorite_color_normal():
    """Test the favorite color function with normal list."""
    normal_dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(normal_dictionary) == "blue"


def test_favorite_color_empty():
    """Test the favorite color functionw with empty list."""
    empty_dictionary: dict[str, str] = {}
    assert favorite_color(empty_dictionary) == ""


def test_favorite_color_tie_list():
    """Test the favorite color function with tied list."""
    tie_dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "David": "yellow"}
    assert favorite_color(tie_dictionary) == "yellow"


def test_count_tie_list():
    """Test the count function with tie list."""
    tie_dictionary: list[str] = ["yellow", "yellow", "green", "green"]
    assert count(tie_dictionary) == {"yellow": 2, "green": 2}


def test_count_normal_list():
    """Test the count function with normal, daily used list."""
    normal_list: list[str] = ["yellow", "green", "red", "yellow", "green", "yellow"]
    assert count(normal_list) == {"yellow": 3, "green": 2, "red": 1}


def test_count_empty_list():
    """Test the count function with empty list."""
    empty_list: list[str] = []
    assert count(empty_list) == {}
