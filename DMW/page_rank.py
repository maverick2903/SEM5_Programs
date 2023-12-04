import numpy as np

def pagerank(num_nodes, adjacency_matrix, damping_factor, max_iterations=100, tolerance=1e-6):
    """
    Parameters:
    - num_nodes: Number of web pages.
    - adjacency_matrix: NumPy 2D array representing the link structure of the web pages.
    - damping_factor: Probability of following a link (default is 0.85).
    - max_iterations: Maximum number of iterations (default is 100).
    - tolerance: Convergence threshold (default is 1e-6).

    Returns:
    - pagerank_scores: NumPy array containing the PageRank scores for each web page.
    """

    # Normalize the adjacency matrix to represent transition probabilities
    row_sums = np.sum(adjacency_matrix, axis=1)
    transition_matrix = adjacency_matrix / np.where(row_sums[:, np.newaxis] == 0, 1, row_sums[:, np.newaxis])

    # Initialize PageRank scores
    pagerank_scores = np.ones(num_nodes) / num_nodes

    # Iterative computation of PageRank scores
    for _ in range(max_iterations):
        prev_pagerank_scores = pagerank_scores.copy()
        pagerank_scores = (1 - damping_factor) / num_nodes + damping_factor * np.dot(transition_matrix.T, pagerank_scores)

        # Check for convergence
        if np.linalg.norm(prev_pagerank_scores - pagerank_scores, 2) < tolerance:
            break

    return pagerank_scores

# Get input from the user
num_nodes = int(input("Enter the number of web pages: "))
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

print("Enter the adjacency matrix (row-wise, space-separated):")
for i in range(num_nodes):
    adjacency_matrix[i] = list(map(int, input().split()))

damping_factor = float(input("Enter the damping factor (default is 0.85): "))

# Compute PageRank scores
scores = pagerank(num_nodes, adjacency_matrix, damping_factor)
print("PageRank Scores:")

for index, s in enumerate(scores):
    print("Site", index, ":", round(s, 3))
