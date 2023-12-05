def best_fit(blocks, processes):
    allocations = {}

    for process in processes:
        best_fit_index = None
        min_remaining_space = float('inf')

        for i, block in enumerate(blocks):
            if block >= process:
                remaining_space = block - process
                if remaining_space < min_remaining_space:
                    min_remaining_space = remaining_space
                    best_fit_index = i

        if best_fit_index is not None:
            allocations[process] = blocks[best_fit_index]
            blocks[best_fit_index] -= process

    return allocations

# Example usage:
blocks = [200, 400, 600, 500, 300, 250]
processes = [357, 210, 468, 491]

allocations = best_fit(blocks, processes)

# Print allocations
for process, block in allocations.items():
    print(f"Process {process} allocated to Block {block}")

# Print remaining blocks
print("Remaining block sizes:", blocks)
