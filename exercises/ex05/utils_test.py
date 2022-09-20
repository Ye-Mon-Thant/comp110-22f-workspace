"""Ex05 - Test."""
__author__ = "730548206"


from exercises.ex05.utils import only_evens, sub, concat #Autograder important fact


def test_only_evens_all_empty() -> None:
    """Empty list given."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_negative() -> None:
    """Negative Numbers are given."""
    xs1: list[int] = [-1, -2, -4]
    assert only_evens(xs1) == [-2, -4]


def test_only_evens_mixed() -> None:
    """Mixed numbers are given."""
    xs2: list[int] = [-2, -1, 0, 1, 2, 4]
    assert only_evens(xs2) == [-2, 0, 2, 4]


def test_only_evens_odd() -> None:
    """Odd numbers are given."""
    assert only_evens([-1, 1, 5, 3, 7]) == []


def test_concat_mixed_number_lists() -> None:
    """Concat mixed numbers."""
    xs3: list[int] = [-5, -4, -3]
    xs4: list[int] = [3, 4, 5]
    assert concat(xs3, xs4) == [-5, -4, -3, 3, 4, 5]


def test_concat_positive_number_lists() -> None:
    """Concat positive numbers."""
    xs5: list[int] = [0, 1, 2]
    xs6: list[int] = [3, 4, 5]
    assert concat(xs5, xs6) == [0, 1, 2, 3, 4, 5]


def test_concat_negative_number_lists() -> None:
    """Concat negative numbers."""
    xs3: list[int] = [-5, -4, -3]
    xs4: list[int] = [0, 1, 2, 3]
    assert concat(xs3, xs4) == [-5, -4, -3, 0, 1, 2, 3]


def test_concat_empty() -> None:
    """Concat two empty lists."""
    xs3: list[int] = []
    xs4: list[int] = []
    assert concat(xs3, xs4) == []


def test_sub_empty() -> None:
    """Sub two empty lists."""
    xs5: list[int] = []
    xs6: int = 0
    xs7: int = 5
    assert sub(xs5, xs6, xs7) == []


def test_sub_negative_start_index() -> None:
    """Sub normal list with negative start index and positive end index."""
    xs8: list[int] = [1, 2, 3, 4, 5, 6, 7]
    xs9: int = -2
    xs10: int = 2
    assert sub(xs8, xs9, xs10) == [1, 2]


def test_sub_positive_start_index() -> None:
    """Sub normal list with positive start index and end index."""
    xs11: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    xs12: int = 0
    xs13: int = 4
    assert sub(xs11, xs12, xs13) == [1, 2, 3, 4]


def test_sub_all_negative() -> None:
    """Sub list with negative number with negative start index and end index."""
    xs14: list[int] = [-1, -2, -3, -4, -5]
    xs15: int = -1
    xs16: int = -5
    assert sub(xs14, xs15, xs16) == []
