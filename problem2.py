A = list(map(int, input().split()))
l = len(A)

p, z = 1, 0

for i in A:
    if i == 0:
        z += 1
    else:
        p *= i

if z > 1:
    print([0]*l)
elif z == 1:
    for i in range(l):
        if A[i] == 0:
            A[i] = p
        else:
            A[i] = 0
    print(A)
else:
    for i in range(l):
        A[i] = p / A[i]
    print(A)