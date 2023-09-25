



"""This specially named module makes the package runnable."""
from __future__ import annotations
from exercises.ex09 import constants
from exercises.ex09.model import Model
from exercises.ex09.view_controller import ViewController
from random import random 
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.INFECTED)
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()




constants

"""Constants used through the simulation."""

BOUNDS_WIDTH: int = 400
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: int = 400
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

CELL_RADIUS: int = 15
CELL_COUNT: int = 10
CELL_SPEED: float = 5.0

VUlNERABLE: int = 0
INFECTED: int = 1




Model


"""The model classes maintain the state and logic of the simulation."""



__author__ = "730574053"


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
    
    def distance(self, second_point: Point) -> float: 
        result: float = sqrt((self.x - second_point.x)**2 + (self.y -second_point.y)**2)
        return result

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None: 
        self.location = self.location.add(self.direction)
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable == True:
            return "gray"
        if self.is_infected == True:
            return "red"

    def contract_disease(self): 
       self.sickness = constants.INFECTED 
    
    def is_vulnerable(self) -> bool:
        result: bool = False
        if self.sickness == constants.VULNERABLE: 
            result = True
        return result

    def is_infected(self) -> bool:
        result: bool = False
        if self.sickness == constants.INFECTED:
            result = True
        return result

    def contact_with(self, other_cell: Cell):
        if self.constants.INFECTED == True and other_cell.constants.VULNERABLE == True:
            other_cell.contract_disease
        if self.constants.VULNERABLE == True and other_cell.constants.INFECTED == True:
            self.contract_disease


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_count: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        i: int = 0
        if infected_count <= 0:
            raise ValueError("There must be at lease one infected cell.")
        for _ in range(cells): 
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: cell = Cell(start_location, start_direction)
            self.population.append(cell)
        while i < infected_count:
            self.population.pop(cell)
            self.population.append(cell.contract_disease)
            i += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        # TODO
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
            cell.location = constants.MAX_X
            cell.direction.x *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False

    def check_contacts(self):
        j: int = 0
        for cell in population:
            cell: Cell = population[i]
            while i > j:
                    result: float = sqrt((cell.x - population[j].x)**2 + (cell.y - population[j].y)**2)
            i += 1

            population[i]

        return None



    ViewController
"""The ViewController drives the visualization of the simulation.""" 

from turtle import Turtle, Screen, _Screen, done
from exercises.ex09.model import Model
from exercises.ex09 import constants
from typing import Any
from time import time_ns


NS_TO_MS: int = 1000000


class ViewController:
    """This class is responsible for controlling the simulation and visualizing it."""
    screen: _Screen
    pen: Turtle
    model: Model

    def __init__(self, model: Model):
        """Initialize the VC."""
        self.model = model
        self.screen = Screen()
        self.screen.setup(constants.VIEW_WIDTH, constants.VIEW_HEIGHT)
        self.screen.tracer(0, 0)
        self.screen.delay(0)
        self.screen.title("Contagion Simulation - EX09")
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)

    def start_simulation(self) -> None:
        """Call the first tick of the simulation and begin turtle gfx."""
        self.tick()
        done()

    def tick(self) -> None:
        """Update the model state and redraw visualization."""
        start_time = time_ns() // NS_TO_MS
        self.model.tick()
        self.pen.clear()
        for cell in self.model.population:
            self.pen.penup()
            self.pen.goto(cell.location.x, cell.location.y)
            self.pen.pendown()
            self.pen.color(cell.color())
            self.pen.dot(constants.CELL_RADIUS)
        self.screen.update()

        if self.model.is_complete():
            return
        else:
            end_time = time_ns() // NS_TO_MS
            next_tick = 30 - (end_time - start_time)
            if next_tick < 0:
                next_tick = 0
            self.screen.ontimer(self.tick, next_tick)