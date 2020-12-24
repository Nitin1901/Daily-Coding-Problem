arr = list(map(int, input("Enter the array: ").split()))

i, j = arr[0], 0

for k in arr[1:]:
    j_ = max(i, j)
    i = (j + k)
    j = j_

print(max(i, j))