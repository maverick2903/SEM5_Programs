#Direct addressing

MOV AX, [1000h]
MOV BX, [1002h]
MOV CL, 00h

ADD AX,BX

MOV [1004h],AX
JNC carry:
INC CL

carry:
MOV [1006h],CL

HLT
ret

#Immdediate addressing

MOV AX, 1000h
MOV BX, 1002h
MOV CL, 00h

ADD AX,BX

MOV DX,AX
JNC carry:
INC CL

carry:

HLT
ret