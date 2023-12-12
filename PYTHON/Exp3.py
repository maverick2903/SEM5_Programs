
def histogram(l):
    count = {}
    for i in l:
       if i not in count:
           count[i] = l.count(i)
    
    final = list(zip(count.keys(),count.values()))
    sort_final = sorted(final,key=lambda x: (x[1],x[0]))
    return sort_final

ans = histogram([1,2,2,3,4,4,4,5,5])
print(ans)

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum += i
    if sum == n: print("Perfect") 
    else: print("Not perfect")

perfect(28)

def tower_of_hanoi(n, source, auxiliary, target):
    if n==1:
        print(f"Move disk {n} from {source} to {target}")
    else:
        tower_of_hanoi(n-1,source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n-1, auxiliary, source, target)

tower_of_hanoi(3,'A','B','C')

a,b = 10,5
grt = lambda x,y: max(x,y)
print(grt(a,b))

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

fun = lambda x,y:x+y
add = list(map(fun,l1,l2))
print(add)

l3 = [1,2,3,4,5]
l4 = filter(lambda x: x%2 != 0,l3)
cube = list(map(lambda x: pow(x,3),l4))
print(cube)