M = '1011'
Q = '1101'
A = '0000'
C = '0'

for _ in range(4):
    if Q[-1] == '1':
        A = bin(int(A,2) + int(M,2)) [2:]
        A = '0'*(4-len(A)) + A
    flag = 0
    if len(A) > 4:
        flag = 1
        A = A[1:]
    if flag == 1: C='1'
    print(A)
    #Shift
    Q = A[-1] + Q[:-1]
    A = C + A[:-1]
    C = '0'
    print(Q)
    print()

print(f"A: {A}, Q: {Q}")
AQ = A+Q
print(f"Answer is: {AQ} - {int(AQ,2)}")