def numWays(n, ways):
    if n == 0:
        return 1
    arr = [1]
    for i in range(1, n+1):
        total = 0
        for j in ways:
            if i >= j:
                total += arr[i-j]
        arr.append(total)
    return arr[-1]

n = int(input("Enter the number of steps: "))
ways = set([int(i) for i in input("Enter the possible steps: ").split()])
print(numWays(n, ways))