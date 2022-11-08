# Cubix
## Overview
A simple Rubik's Cube simulator and solver built in Python with Pygame for visual rendering and performance analysis of various cube solving algorithms.

### Features
* Two-dimensional visualisation of a 3x3 Rubik's cube
* Keyboard controls for face turns and rotations.
* Generation of animated solutions based on the user selected method.

## Quick Start
To work on or run this project, start by creating a virtual environment:
```
$ virtualenv venv
```

Activate the virtual environment by running:
```
$ source venv/bin/activate
```

Install the dependencies inside the virtual environment
```
$ pip install -r requirements.txt
```

Launch the main graphical user interface
```
$ python3 -m src.main
```

## Repository Structure
### ``src/cube``
This folder contains the majority of the core logic for representing the Cube and the solver.
- ``gui.py`` - The **Gui class** which acts as the interface between the **Cube class** and **Pygame**.
- ``cube.py`` - The **Cube class** which encapsulates all the main logic for representing a Rubik's Cube.
- ``history_cube.py`` - A **subclass of Cube** that has methods to record all moves applied.
- ``solver.py`` - The **solving functions** that generate solutions given an instance of a **Cube**.
- ``move.py`` - A simple **Move dataclass** to encapsulate information about specific moves.
- ``pieces.py`` - Simple **Edge and Corner dataclasses** to encapsulate information about pieces.
- ``colour.py`` - A simple **Colour type definition** to wrap around RGB colour tuples.

### ``src/scramble``
This folder contains any logic regarding scramble generation and scramble parsing.
- ``generator.py`` - A simple **scramble generation function** that randomly selects moves to produce a scramble.
- ``parser.py`` - A set of **parsing functions** to convert between moves of **str** type and **Move** type.

### ``src/p2``
This folder contains code for all the search algorithms and the heurestics required by them.
- ``AIs.py`` - Comtains the implementaion of all the **Search Algorithms** that user selectable to solve a scramble.
- ``Cubeai.py`` - A set of **Cube functions** to simulate the cube necesary for the search algorithms to work on.
- ``Heuristics.py`` - All the implementations of **Heuristics** that are user slectable.
- ``ManhattanCube.py`` - A helper funtion to create the **Manhattan Cube** necessary for the Manhattan Hueristics to work.
 
## Implementation ##
### Cube ###
This program uses a relatively simplistic representation of the Rubik's Cube. We simply consider the cube to be an array of 6 2-dimensional arrays, each representing a face of the cube. Each element of these 2-dimensional arrays then represents a sticker on the cube.

A single face turn then can be implemented by:

1. Rotating all elements of the given face by 90 degrees
2. Cycling all the rows/columns that intersect with the given face on all adjacent faces

### Solving ###
The program implements a collection of search algorithms and also includes Kociemba and the traiditional Beginners method(Layering) to provide a wide diversity for the user to choose between and solve the scramble and have a visualization of the performance and solution of each algorithm.
