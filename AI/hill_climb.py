
# import random

# def random_solution(tsp):
#     cities = list(range(len(tsp)))
#     solution = []
#     for i in range(len(tsp)):
#         random_city = cities[random.randint(0, len(cities) - 1)]
#         solution.append(random_city)
#         cities.remove(random_city)
#     return solution

# def route_length(tsp, solution):
#     length = 0
#     for i in range(len(solution)):
#         length += tsp[solution[i - 1]][solution[i]]
#     return length

# def get_neighbours(solution):
#     neighbours = []
#     for i in range(len(solution)):
#         for j in range(i + 1, len(solution)):
#             neighbour = solution.copy()
#             neighbour[i] = solution[j]
#             neighbour[j] = solution[i]
#             neighbours.append(neighbour)
#     return neighbours

# def get_best_neighbour(tsp, neighbours):
#     best_length = route_length(tsp, neighbours[0])
#     best_neighbour = neighbours[0]
#     for neighbour in neighbours:
#         current_length = route_length(tsp, neighbour)
#         if current_length < best_length:
#             best_length = current_length
#             best_neighbour = neighbour
#     return best_neighbour, best_length

# def hill_climbing(tsp):
#     current_solution = random_solution(tsp)
#     current_length = route_length(tsp, current_solution)
#     neighbours = get_neighbours(current_solution)
#     best_neighbour, best_length = get_best_neighbour(tsp, neighbours)
#     while best_length < current_length:
#         current_solution = best_neighbour
#         current_length = best_length
#         neighbours = get_neighbours(current_solution)
#         best_neighbour, best_length = get_best_neighbour(tsp, neighbours)
#     return current_solution, current_length

# def main():
#     tsp = [
#         [0, 100, 700, 50],
#         [100, 0, 330, 1200],
#         [700, 330, 0, 400],
#         [50, 1200, 400, 0]
#     ]
#     print(hill_climbing(tsp))

# if __name__ == "__main__":
#     main()

def f(x):
    value = x
    return value


def hillclimb():
    graph = [
        [5, 12, 8, 3, 19, 25, 10, 7],
        [15, 22, 18, 13, 29, 35, 20, 17],
        [25, 32, 28, 23, 39, 45, 30, 27],
        [35, 42, 38, 33, 49, 55, 40, 37],
        [45, 52, 48, 43, 59, 65, 50, 47],
        [55, 62, 58, 53, 69, 75, 60, 57],
        [65, 72, 68, 63, 79, 85, 70, 67],
        [75, 82, 78, 73, 89, 95, 80, 77]
    ]

    state = [0, 0]
    max_val = float('-inf')
    while True:
        old_val = max_val
        x = state[0]
        y = state[1]
        possible_moves = [[x+1, y], [x-1, y], [x+1, y+1],
                          [x-1, y-1], [x+1, y-1], [x-1, y+1], [x, y-1], [x, y+1]]
        for x1, y1 in possible_moves:
            if 0 <= x1 < 8 and 0 <= y1 < 8:
                val = f(graph[x1][y1])
                if val > max_val:
                    print(val)
                    max_val = val
                    state = [x1, y1]
        if old_val == max_val:
            print(state)
            break

    print(f"Max Value is {max_val} at state {state}")


hillclimb()