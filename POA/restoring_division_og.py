A = '00000'
M = input("Enter Divisor: ")
Q = input("Enter Dividend: ")


M_minus = ''

for i in M:
    if i == '0':
        M_minus += '1'
    else: M_minus += '0'

M_minus = bin(int(M_minus,2) + 1)[2:]
M_minus = '0'*(5 - len(M_minus)) + M_minus

for i in range(5):
    A = A[1:] + Q[0]
   
   
    A = bin(int(A,2) + int(M_minus,2))[2:]
    if len(A) > 5:
        A = A[1:]
    A = '0'*(5 - len(A)) + A

    if A[0] == '1':
        Q = Q[1:] + '0'
        A = bin(int(A,2) + int(M,2))[2:]

        if len(A) > 5:
            A = A[1:]
        A = '0'*(5 - len(A)) + A

    else:
        Q = Q[1:] + '1'


print("Remainder: ")
print(A)
print(int(A,2))
print("\nQuotient: ")
print(Q)
print(int(Q,2))