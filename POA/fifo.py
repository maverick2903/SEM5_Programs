def lru_page_replacement(page_references, frame_size):
    page_frames = []  # List to store the pages currently in memory
    page_order = []   # List to store the order of page usage
    page_faults = 0   # Counter for page faults
    page_hits = 0     # Counter for page hits

    print("Initial Page Reference:", page_references)
    print("\nSteps:")
    
    for page in page_references:
        # If the page is not in memory, it's a page fault
        if page not in page_frames:
            # If the number of frames is equal to the frame size, remove the least recently used page
            if len(page_frames) == frame_size:
                lru_page = page_order.pop(0)
                page_frames.remove(lru_page)
                print(f"Page {lru_page} removed from memory (Miss)")
            # Add the new page to memory
            page_frames.append(page)
            page_order.append(page)
            print(f"Page {page} added to memory (Miss)")
            page_faults += 1
        else:
            # If the page is already in memory, update its usage order
            page_order.remove(page)
            page_order.append(page)
            print(f"Page {page} already in memory (Hit)")
            page_hits += 1

    total_pages = len(page_references)
    hit_ratio = page_hits / total_pages * 100

    print("\nResults:")
    print(f"Total Hits: {page_hits}")
    print(f"Total Faults: {page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}%")

# Example usage:
page_references = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
frame_size = 3

lru_page_replacement(page_references, frame_size)