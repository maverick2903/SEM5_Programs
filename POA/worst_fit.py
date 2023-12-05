def worst_fit(blocks, processes):
    allocations = {}

    for process in processes:
        worst_fit_index = None
        max_remaining_space = -1

        for i, block in enumerate(blocks):
            if block >= process:
                remaining_space = block - process
                if remaining_space > max_remaining_space:
                    max_remaining_space = remaining_space
                    worst_fit_index = i

        if worst_fit_index is not None:
            allocations[process] = blocks[worst_fit_index]
            blocks[worst_fit_index] -= process

    return allocations

# Example usage:
blocks = [200, 400, 600, 500, 300, 250]
processes = [357, 210, 468, 491]

allocations = worst_fit(blocks, processes)

# Print allocations
for process, block in allocations.items():
    print(f"Process {process} allocated to Block {block}")

# Print remaining blocks
print("Remaining block sizes:", blocks)
