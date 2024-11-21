# Simulated-Annealing-in-Latin-Square

Latin Square Solver Using Simulated Annealing

Overview
This Python program generates and optimizes a Latin square using the Simulated Annealing algorithm. A Latin square is an n×n grid where each cell contains a value, and no value is repeated in any row or column. This project implements a heuristic method to minimize the conflicts in rows and columns to approach a valid Latin square.

Features:

Initial Solution Generation:
Generates a random n×n Latin square as the starting solution.

Cost Function:
Evaluates the "cost" of the Latin square based on duplicate values in rows and columns.

Simulated Annealing Algorithm:
Iteratively improves the solution using a probabilistic acceptance criterion to escape local minima.

Neighbor Generation:
Generates new candidate solutions by swapping two random cells in the grid.

Parameters:
Supports customizable initial temperature, cooling rate (α), and freezing factor.

Usage Instructions:
Run the Program: Execute the program by running:
python3 <filename>.py

Input Requirements:
Enter an even integer value for n between 4 and 20.
The program will terminate if n is invalid.

Adjustable Parameters:
Modify the following variables in the main() function for tuning:
alpha: Cooling rate (default: 0.99).
freezing_factor: Determines when the algorithm halts (default: 1000).
