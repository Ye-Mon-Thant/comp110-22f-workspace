"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730548206"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty list should raise a ValueError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_normal() -> None:
    """Value_at of a normal list should return the value of the indexed numbered Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_value_at_out_of_index() -> None:
    """Value_at of a normal list with over-index should return Index Error."""
    with pytest.raises(IndexError):
        value_at(Node(1, Node(2, Node(3, None))), 4)


def test_max_normal() -> None:
    """Max of a normal list should return the biggest value in linked list."""
    linked_list = Node(3, Node(0, Node(2, None)))
    assert max(linked_list) == 3


def test_max_empty() -> None:
    """Max of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_normal() -> None:
    """Linkify of a normal list should return a linked list."""
    assert str(linkify([1, 2, 3])) == "1 -> 2 -> 3 -> None"


def test_linkify_empty() -> None:
    """Linkify of an empty list should return None."""
    assert linkify([]) is None


def test_scale_normal() -> None:
    """Scale of a normal list should return a linked list with values multiplied."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"


def test_scale_empty() -> None:
    """Scale of an empty list should return None."""
    assert scale(None, 2) is None
