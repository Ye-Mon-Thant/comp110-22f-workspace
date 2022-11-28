"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730548206"


class Simpy:
    """Simpy class with an initial list of floats called 'values'."""
    values: list[float]

    def __init__(self, given_list: list[float]):
        """Initialize the class by assigning 'given_list' into 'values'."""
        self.values = given_list

    def __repr__(self) -> str:
        """Returns string for computers."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill up the 'values' list of class with 'times' times 'value'."""
        self.values = []
        for _ in range(times):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Works similar to built-in range function but with float steps."""
        assert step != 0.0
        controller: bool = True
        value: float = start
        while controller:
            if (value < stop and step > 0) or (value > stop and step < 0):
                self.values.append(value)
            else:
                controller = False
            value += step

    def sum(self) -> float:
        """Returns sum of the values of the list of the class."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add every element of list of class with a constant float or respective floats of rhs."""
        result_list: list[float] = []
        if isinstance(rhs, float):
            for s in self.values:
                result_list.append(s + rhs)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result_list.append(self.values[i] + rhs.values[i])
        return Simpy(result_list)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponents the original class list to the constant rhs or respective constants of rhs(simpy)."""
        result_list: list[float] = []
        if isinstance(rhs, float):
            for i in self.values:
                result_list.append(i ** rhs)
        else:
            assert len(rhs.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_list.append(self.values[i] ** rhs.values[i])
        return Simpy(result_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns list of the elements of the class list that equals to the rhs or respective rhs values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for s in range(len(self.values)):
                result.append(self.values[s] == rhs.values[s])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Respective values of class list greater than rhs or respective rhs values return True."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for s in range(len(self.values)):
                result.append(self.values[s] > rhs.values[s])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns the specific rhs indexed value or the new simpy with values having same index as Trues."""
        if isinstance(rhs, int):
            if rhs > len(self.values):
                raise IndexError
            else:
                return self.values[rhs]
        else:
            result: list[float] = []
            assert len(rhs) == len(self.values)
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result) 
