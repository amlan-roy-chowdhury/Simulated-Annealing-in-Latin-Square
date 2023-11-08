import copy
import random
import math

# Function to generate an initial random Latin square
def generate_initial_solution(n):
    num_elements = n * n
    latin_square = []
    for i in range (n):
        temp = [i for i in range (1, n+1)]
        random.shuffle (temp)
        latin_square.append (temp)
    # latin_square = []
    #
    # for i in range(1, num_elements + 1):
    #     latin_square.append(i)
    #
    #     random.shuffle(latin_square)


    return latin_square


# latin_square = generate_initial_solution(n)
# Function to calculate the cost of a Latin square
def calculate_cost(latin_square):

    n = len(latin_square)

    cost = 0

    # Check for conflicts in rows

    for row in latin_square:

        cost += len(row) - len (set(row))

        #for col in range(n):

            #value = latin_square[row * n + col]

            #if value in row_values:
                #cost += 1  # Duplicate value in the same row

            #ow_values.add(value)

    # Check for conflicts in columns

    for col in zip (*latin_square):

        cost += len(col) - len (set(col))

        # for row in range(n):
        #
        #     value = latin_square[row * n + col]
        #
        #     if value in col_values:
        #         cost += 1  # Duplicate value in the same column
        #
        #     col_values.add(value)

    return cost


def calculate_probability(neighbor_cost, current_cost, temperature):
    return math.exp(-(neighbor_cost - current_cost) / temperature)


# Function to generate initial temperature
def calculate_initial_temp(n):
    return n^2

# Function to generate a neighbor by swapping two elements
def generate_neighbor(latin_square):
    i1 = i2 = j1 = j2  = 0
    while i1 == i2 and j1 == j2:
        i1, j1 = random.randint(0, len(latin_square) - 1), random.randint(0, len(latin_square) - 1)
        i2, j2 = random.randint(0, len(latin_square) - 1), random.randint(0, len(latin_square) - 1)
    #
    # if i1 == i2 and j1 == j2:
    #     print("NO SWAP")

    # Swap the values of the two cells.
    latin_square[i1][j1], latin_square[i2][j2] = latin_square[i2][j2], latin_square[i1][j1]

    return latin_square

# Simulated Annealing algorithm
def simulated_annealing(n, initial_temp, alpha, freezing_factor):
    best_solution = generate_initial_solution(n)
    best_cost = calculate_cost(best_solution)

    current_solution = copy.deepcopy(best_solution)
    current_cost = best_cost
    iterations = 0
    temperature = initial_temp
    phi_counter = 0

    while phi_counter < freezing_factor:
        neighbors = []
        best_solution_changed = False
        for _ in range(3):  # Generate 3 random neighbors
            while True:
                neighbor = generate_neighbor(copy.deepcopy(current_solution))
                if neighbor not in neighbors:
                    break
            neighbors.append(neighbor)

        best_neighbor = neighbors[0]
        best_neighbor_cost = calculate_cost(neighbors[0])

        for neighbor in neighbors[1:]:
            if (cost := calculate_cost(neighbor)) < best_neighbor_cost:
                best_neighbor_cost = cost
                best_neighbor = neighbor

        if best_neighbor_cost > current_cost:
            # Acceptance probability
            best_neighbor = neighbors[0]
            best_neighbor_cost = calculate_cost(neighbors[0])
            best_neighbor_probability = calculate_probability(best_neighbor_cost, current_cost, temperature)
            # best_neighbor_probability = math.exp(-(best_neighbor_cost - current_cost) / temperature)
            for neighbor in neighbors[1:]:
                if (probability := calculate_probability(calculate_cost(neighbor), current_cost, temperature)) > best_neighbor_probability:
                    best_neighbor_probability = probability
                    best_neighbor = neighbor
                    best_neighbor_cost = calculate_cost(neighbor)

        current_solution = best_neighbor
        current_cost = best_neighbor_cost

        if best_neighbor_cost < best_cost:
            best_solution = best_neighbor
            best_cost = best_neighbor_cost
            best_solution_changed = True

        temperature *= alpha
        iterations += 1

        if best_solution_changed:
            phi_counter = 0
        else:
            phi_counter += 1

        if current_cost == 0:
            print("Complete solution reached:")
            print(current_solution)
            print(f"Cost: {current_cost}")
            print(f"Iterations: {iterations}")
            return current_solution, current_cost, iterations
        elif int(temperature) <= 0:
            print("Final temperature reached:")
            print(best_solution)
            print(f"Least Cost: {best_cost}")
            print(f"Iterations: {iterations}")
            return best_solution, best_cost, iterations

    print("Freezing factor reached:")
    print(best_solution)
    print(f"Least Cost: {best_cost}")
    print(f"Iterations: {iterations}")

    return best_solution, best_cost, iterations


def main():
    n = int(input("Enter the value of n (even number between 4 and 20): "))

    if n % 2 != 0 or n < 4 or n > 20:
        print("Invalid input. n must be an even number between 4 and 20.")
        return

    initial_temp = calculate_initial_temp(n)  # Implement this function
    alpha = 0.99
    freezing_factor = 1000  # adjustable value

    simulated_annealing(n, initial_temp, alpha, freezing_factor)


# main()
if __name__ == "__main__":
    main()