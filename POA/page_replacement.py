size = 3
pages = [2, 3, 5, 3, 2, 1, 3, 4, 2, 5]

def fifo():
    hits, faults = 0, 0
    frame = []
    for p in pages:
        if len(frame)<3:
            frame.append(p)
            faults += 1
            print(f'{frame}: Fault')
        else:
            if p in frame:
                hits += 1
                print(f'{frame}: Hit')
            else:
                frame.pop(0)
                frame.append(p)
                faults += 1
                print(f'{frame}: Fault')
    return hits,faults

def lru():
    hits, faults = 0, 0
    frame = []
    for p in pages:
        if len(frame)<3:
            frame.append(p)
            faults += 1
            print(f'{frame}: Fault')    
        else:
            if p in frame:
                hits += 1
                print(f'{frame}: Hit')
                frame.remove(p)
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)
                faults += 1
                print(f'{frame}: Fault')
    return hits,faults                

hits,faults = fifo()
print(f"Number of hits: {hits}")
print(f"Number of faults: {faults}") 

hits,faults = lru()
print(f"Number of hits: {hits}")
print(f"Number of faults: {faults}") 
