import numpy as np

def hits_algorithm(adj_matrix, num_iterations):
    num_nodes = len(adj_matrix)
    authority_scores = np.ones(num_nodes)
    hub_scores = np.ones(num_nodes)

    print("Initial Authority Scores:", authority_scores)
    print("Initial Hub Scores:", hub_scores)

    for iteration in range(num_iterations):
        authority_scores_new = np.dot(adj_matrix.T, hub_scores)
        hub_scores_new = np.dot(adj_matrix, authority_scores_new)

        authority_scores = authority_scores_new / np.linalg.norm(authority_scores_new)
        hub_scores = hub_scores_new / np.linalg.norm(hub_scores_new)

        print("Iteration", iteration+1)
        print("Authority Scores:", authority_scores)
        print("Hub Scores:", hub_scores)
        print()

num_nodes = int(input("Enter the number of nodes: "))
adj_matrix = np.zeros((num_nodes, num_nodes))
for i in range(num_nodes):
    for j in range(num_nodes):
        adj_matrix[i][j] = int(input(f"Enter the adjacency value for node {i+1} and node {j+1}: "))

num_iterations = int(input("Enter the number of iterations: "))

hits_algorithm(adj_matrix, num_iterations)
