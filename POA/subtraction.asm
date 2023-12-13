#Subtraction using direct addressing

MOV AX, [1000h]
MOV BX, [1002h]
MOV CL, 00h

SUB AX,BX

MOV [1004h], AX
JNC not_carry:
INC CL
NOT AX
INC AX

not_carry:
MOV [1006h],CL

HLT
ret

#Subtraction using immediate addressing
MOV AX, 1000h
MOV BX, 1002h
MOV CL, 00h

SUB AX,BX

JNC not_carry:
INC CL
NOT AX
INC AX

not_carry:
MOV DX, AX

HLT
ret
