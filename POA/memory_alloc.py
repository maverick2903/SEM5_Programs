
def bestfit():
    memory = [200, 400, 600, 500, 300, 250]
    processes = [357, 210, 468, 491]
    for proc in processes:
        min_diff = float('inf')
        min_mem = 0
        for mem in memory:
            if mem-proc < min_diff and mem-proc>0:
                min_diff = mem-proc
                min_mem = mem
        memory.remove(min_mem)
        print(f"Process {proc} goes in memory {min_mem}")

def worstfit():
    memory = [200, 400, 600, 500, 300, 250]
    processes = [357, 210, 468, 491]
    memory.sort(reverse=True)
    for proc in processes:
        if memory[0] - proc > 0:
            print(f"Process {proc} goes in memory {memory[0]}")
            memory.remove(memory[0])        

        
        
bestfit()
print()
worstfit()