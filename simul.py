from P1_achowd20 import simulated_annealing

import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(("Best Solution", "Best Cost", "Iterations"))
    for _ in range(10):
        n = 20
        #max_iterations = 64  # adjustable value
        initial_temp = 400 # Implement this function
        alpha = 0.99
        freezing_factor = 500  # adjustable value

        writer.writerow(simulated_annealing(n, initial_temp, alpha, freezing_factor))