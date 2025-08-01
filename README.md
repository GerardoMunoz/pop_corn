# PopCorn: A MicroPython Framework for Simulation, Machine Learning, and Visualization
* https://github.com/GerardoMunoz/pop_corn
* https://youtube.com/shorts/q8LiIZUanPs?si=thUsrglDgBfzkSmU

## Overview
PopCorn is a framework designed to create modules for MicroPython using Object-Oriented Programming. This approach enables the same program to drive different peripherals seamlessly. For example, you can use the same command to draw on an OLED display, in Tkinter, or on an HTML canvas through a MicroPython web server.

## Applications
The following files contain applications that can be executed after downloading or cloning the entire project:

### Billiard Simulation
- **billar_tkinter.py** – Simulates collisions and viscosity forces between discs using Tkinter.
- **billar_upy_html.py** – Simulates collisions and viscosity forces between discs using an HTML canvas on a MicroPython web server.

### Line Follower Simulation
- **line_follower_tkinter.py** – Simulates a car following a line using Tkinter.
- **line_fol_perc_tkinter.py** – Simulates a line follower using a perceptron-based learning approach in Tkinter.
- **line_fol_reinf_tkinter.py** – Simulates a line follower using reinforcement learning in Tkinter.

### Finite State Machine Simulation
- **states_tkinter.py** – Simulates a finite state machine using Tkinter.

## Directory Structure
- **img/** – Contains images and utilities to convert images to matrix format.
- **py/** – Contains files that cannot be executed in MicroPython.
- **upy/** – Contains files that cannot be executed on a computer.

## Contribution Guidelines
To collaborate, please fork the repository, create a new branch for your changes, and submit a pull request. Contributions, issues, and feature requests are welcome.

In the [Issues section](https://github.com/GerardoMunoz/pop_corn/issues), you can report bugs, suggest new features, or discuss current and upcoming changes. Your feedback and participation are highly valued!


