
import random

def random_solution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    for i in range(len(tsp)):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)
    return solution

def route_length(tsp, solution):
    length = 0
    for i in range(len(solution)):
        length += tsp[solution[i - 1]][solution[i]]
    return length

def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def get_best_neighbour(tsp, neighbours):
    best_length = route_length(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_length = route_length(tsp, neighbour)
        if current_length < best_length:
            best_length = current_length
            best_neighbour = neighbour
    return best_neighbour, best_length

def hill_climbing(tsp):
    current_solution = random_solution(tsp)
    current_length = route_length(tsp, current_solution)
    neighbours = get_neighbours(current_solution)
    best_neighbour, best_length = get_best_neighbour(tsp, neighbours)
    while best_length < current_length:
        current_solution = best_neighbour
        current_length = best_length
        neighbours = get_neighbours(current_solution)
        best_neighbour, best_length = get_best_neighbour(tsp, neighbours)
    return current_solution, current_length

def main():
    tsp = [
        [0, 100, 700, 50],
        [100, 0, 330, 1200],
        [700, 330, 0, 400],
        [50, 1200, 400, 0]
    ]
    print(hill_climbing(tsp))

if __name__ == "__main__":
    main()
