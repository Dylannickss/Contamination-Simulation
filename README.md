# Contamination-Simulation

Pathogen Spread Simulation

This code snippet represents a simple simulation of a pathogen spreading through a population. It utilizes Python's Turtle graphics library to visualize the simulation in a window.

This simulation consists of the following components:

Constants
BOUNDS_WIDTH: Width of the simulation window.
BOUNDS_HEIGHT: Height of the simulation window.
MAX_X, MIN_X: Maximum and minimum X-coordinate values within the simulation window.
MAX_Y, MIN_Y: Maximum and minimum Y-coordinate values within the simulation window.
VIEW_WIDTH, VIEW_HEIGHT: Width and height of the visualization window.
CELL_RADIUS: Radius of the cells in the simulation.
CELL_COUNT: Number of cells in the population.
CELL_SPEED: Speed at which cells move.
VULNERABLE: A constant representing a vulnerable cell state.
INFECTED: A constant representing an infected cell state.

Point
A class representing a 2-dimensional cartesian coordinate point.
Provides methods for adding points and calculating the distance between two points.

Cell
Represents an individual subject in the simulation.
Contains methods for moving a cell (tick), determining its color, contracting disease, and checking its vulnerability and infection status.
Handles cell interactions and disease spreading with other cells.

Model
Represents the state of the simulation.
Initializes the cells with random locations and directions, including infected cells.
Provides methods for updating the simulation state, enforcing bounds, checking if the simulation is complete, and checking for cell contacts.

ViewController
Drives the visualization of the simulation using Turtle graphics.
Initializes the visualization window and controls the simulation's main loop.
Provides methods for updating the visualization and handling the simulation's timing.
How the Simulation Works

The simulation creates a population of cells with random initial positions and directions.
Some cells are initialized as infected, while others are vulnerable.
The simulation runs in a loop, where each iteration represents a time step.
Cells move randomly within the simulation window.
Infected cells can spread the disease to vulnerable cells upon contact.
The simulation continues until a specified condition is met.
Additional Notes

The code is organized into modules for better readability and maintainability.
The Turtle graphics library is used for visualization, making it suitable for educational purposes.
The simulation's behavior can be customized by modifying the constants and logic in the code.
Please refer to the code comments and documentation for more details on each component and its functionality.
