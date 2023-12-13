
# def booth(a, m, q, q1, n, n_len):
#     print(f"{n}\t{a}\t\t{q}\t\t{q1}")
#     if n == 0:
#         return f"Answer : {a,q} deci : {int(a+q, 2)}" if a[0] == '0' else f"Answer is negative : {a,q}\n 2's Complement : {complement(a+q)}\n deci : {int(complement(a+q),2)}"
#     if q[-1] == "1" and q1[-1] == '0':
#         print('10 <-')
#         a = add(a,complement(m.zfill(n_len)))
#         if len(a) != n_len:
#             a = a[1:]
#         print(f"{n}\t{a}\t\t{q}\t\t{q1}\t before ars")
#         a,q,q1 = ars(a,q,q1)
#     elif q[-1] == '0' and q1[-1] == '1':
#         print('01 <-')
#         a = add(a,m)
#         if len(a) != n_len:
#             a = a[1:]
#         print(f"{n}\t{a}\t\t{q}\t\t{q1}\t before ars")
#         a,q,q1 = ars(a,q,q1)
#     elif (q[-1] == '1' and q1[-1] =='1') or (q[-1] =='0' and q1[-1] == '0'):
#         print('00 or 11 <-')
#         a,q,q1 = ars(a,q,q1)
#     return booth(a, m, q, q1, n-1, n_len)

# def complement(a):
#     res = ""
#     for i in a:
#         if i == '1':
#             res += '0'
#         elif i == '0':
#             res += '1'
#     res = add(res,'1')
#     return res

# def ars(a,q,q1):
#     q1 = q[-1]
#     q = a[-1] + q[:-1]
#     a = a[0] + a[:-1]
#     return a,q,q1

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

# a = int(input("Enter Q : "))
# b = int(input("Enter M : "))
# n = len(bin(max(abs(a),abs(b)))[2:]) + 1
# a = bin(a)[2:].zfill(n) if a >= 0 else complement(bin(a)[3:].zfill(n))
# b = bin(b)[2:].zfill(n) if b >= 0 else complement(bin(b)[3:].zfill(n))
# print(f"M = {a}, Q = {b}, A={'0'*n}, Count={n}")
# print("Count\tA\t\tQ\t\tQ1")
# print("---------------------------------------------------------------")
# print(booth('0'*n, a.zfill(n), b.zfill(n), '0', n, n))

#Easier Booth's implementation
# M = input('Enter M: ')
# Q = input('Enter Q: ')
M = '0111'
Q = '1101'
A = '0000'
Q1 = '0'
M_minus = ''

for bit in M:
    if bit=='0':
        M_minus += '1'
    else: M_minus += '0'

M_minus = bin(int(M_minus,2) + 1)[2:]
M_minus = '0'*(4-len(M_minus)) + M_minus

print(M_minus)

for i in range(4):
    if Q[-1]=='1' and Q1=='0':
        A = bin(int(A,2) + int(M_minus,2)) [2:]
        A = '0'*(4-len(A)) + A

    elif Q[-1]=='0' and Q1=='1':
        A = bin(int(A,2) + int(M,2)) [2:]
        A = '0'*(4-len(A)) + A

    if len(A) > 4:
        A = A[1:]
    print(A)
    #ARS
    Q1 = Q[-1]
    Q =  Q[:-1]
    Q = A[-1] + Q
    A = A[:-1]
    A = A[0] + A

print(f"A: {A}, Q: {Q}")

AQ = A + Q
if AQ[0] == '1':
    AQ_minus = ''
    for bit in AQ:
        if bit=='0':
            AQ_minus += '1'
        else: AQ_minus += '0'

    AQ_minus = bin(int(AQ_minus,2) + 1)[2:]
    AQ_minus = '0'*(4-len(AQ_minus)) + AQ_minus
    print(f"Answer is: {AQ_minus} - {int(AQ_minus,2)}")

else:
    print(f"Answer is: {AQ} - {int(AQ,2)}")