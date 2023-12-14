
# def restoring(a, q, m, n, n_len):
#     print(f"{n}\t{a}\t\t{q}")
#     if n == 0:
#         return f"Quotient : bin : {q} Deci : {int(q,2)}\n Remainder : bin : {a},deci : {int(a,2)}"
#     a, q = lrs(a,q)
#     print(f"{n}\t{a}\t\t{q}\t\tAfter LRS ")
#     a = add(a,complement(m))
#     print(f"{n}\t{a}\t\t{q}\t\tAfter A<- A - M ")
#     if len(a) > n_len:
#         a = a[1:]
#     if a[0] == '1':
#         print("A<0")
#         q = q.replace('_','0')
#         a = add(a,m)
#         if len(a) > n_len:
#             a = a[1:]
#         print(f"{n}\t{a}\t\t{q}\t\tAfter A<- A + M ")
#     else:
#         print("A>0")
#         q = q.replace('_','1')
#     return restoring(a, q, m, n-1,n_len)

# def add(a,b):
#     max_len = max(len(a), len(b))
#     a = a.zfill(max_len)
#     b = b.zfill(max_len)
#     result = ''
#     carry = 0
#     for i in range(max_len - 1, -1, -1):
#         r = carry
#         r += 1 if a[i] == '1' else 0
#         r += 1 if b[i] == '1' else 0
#         result = ('1' if r % 2 == 1 else '0') + result
#         carry = 0 if r < 2 else 1
#     if carry != 0:
#         result = '1' + result
#     return result.zfill(max_len)

# # enter binary in string
# def complement(a):
#     res = ""
#     for i in a:
#         if i == '1' :
#             res += '0'
#         elif i == '0':
#             res += '1'
#     res = add(res,'1')
#     return res

# def lrs(a,q):
#     a = a[1:] +q[0]
#     q = q[1:] +"_"
#     return a,q

# q = int(input("Enter Q : "))
# m = int(input("Enter M : "))

# n = len(bin(max(abs(q),abs(m)))[2:])+1
# q = bin(q)[2:].zfill(n) if q>=0 else complement(bin(q)[3:].zfill(n))
# m = bin(m)[2:].zfill(n) if m>=0 else complement(bin(m)[3:].zfill(n))

# print(q,m)
# print(n)
# print(f"M = {m}, Q = {q}, A={'0'*n}")
# print("Count\tA\t\tQ\t\tAny action")
# print("---------------------------------------------------------------")

# print(restoring('0'*n, q.zfill(n), m, n, n))

Q = '01101'
M = '00101'
A = '00000'
M_minus = ''

for bit in M:
    if bit=='0':
        M_minus += '1'
    else: M_minus += '0'

M_minus = bin(int(M_minus,2) + 1)[2:]
M_minus = '0'*(5-len(M_minus)) + M_minus

for _ in range(5):
    #LS
    A = A[1:] + Q[0]
    Q = Q[1:]

    A = bin(int(A,2) + int(M_minus,2))[2:]
    A = '0'*(5-len(A)) + A

    if len(A) > 5:
        A = A[1:]

    if A[0] == '1':
        Q += '0'
        A = bin(int(A,2) + int(M,2))[2:]
        A = '0'*(5-len(A)) + A
    else:
        Q += '1'

    if len(A) > 5:
        A = A[1:]

    print(A)
    print(Q)
    print()

print(f"Quotient: {A}, {int(A,2)}")
print(f"Remainder: {Q}, {int(Q,2)}")    