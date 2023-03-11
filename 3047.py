M = int(input())

A = int(input())
B = int(input())
C = M - (A + B)

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
print(A)
