"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from math import sqrt
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730548206" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns distance between the two points."""
        distance_between_them: float
        distance_between_them = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance_between_them


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute of the Cell object the method is called on."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Return True when the cell’s sickness attribute is equal to VULNERABLE and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Return True when the cell’s sickness attribute is equal to INFECTED and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str: 
        """Return "gray" if the Cell is vulnerable, and "red" if the Cell is infected."""
        if self.is_infected():         
            return "red"
        elif self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "light blue"
        else:
            return "black"  # To check whether the if-loop goes through this option.

    def contact_with(self, another: Cell) -> None:
        """Either of the Cell objects is infected and the other is vulnerable, then the other becomes infected."""
        if self.is_infected() and another.is_vulnerable():
            another.contract_disease()
        elif self.is_vulnerable() and another.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Assign the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Return True when the Cell object’s sickness attribute is equal to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
        

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_number: int, immune_cells_number: int = 0):
        """Initialize the cells with random locations and directions."""
        if (infected_number <= 0) or (infected_number >= cells) or (immune_cells_number < 0) or \
                (immune_cells_number >= cells) or (infected_number + immune_cells_number >= cells):
            raise ValueError("Some number of the cell objects must begin infected!")
        self.population = []
        i: int = 0
        s: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected_number:
                cell.contract_disease()
                i += 1
            elif s < immune_cells_number:
                cell.immunize()
                s += 1
            else:
                cell.sickness = constants.VULNERABLE
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < -constants.MAX_X:
            cell.location.x = -constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.y < -constants.MAX_Y:
            cell.location.y = -constants.MAX_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Test whether any two Cell values come in “contact” with one another."""
        i: int = 0
        while i < len(self.population):
            for numbers in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[numbers].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[numbers])
            i += 1

    def is_complete(self) -> bool:
        """The state of the simulation is complete when there are no remaining infected cells."""
        for cells in self.population:
            if cells.is_infected():
                return False
            else:
                pass
        return True
