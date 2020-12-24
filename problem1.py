"""
We traverse through the array.
We calculate the number required by subtracting the element from the sum.
If the required number is present in the set, we found the pair.
Add the element to the set.

Example:
    array = [3, 5, 2, 1]
    k = 7
    set = {}

    i = 3
    temp = 4
    4 not in set
    s = {3}

    i = 5
    temp = 2
    2 not in set
    s = {3, 5}

    i = 2
    temp = 5
    5 is in set
    return (5, 2)

Order-wise pair = (temp, i)

Time-complexity = O(n)
Space-complexity = O(n)
"""

def getPair(arr, k):
    for i in arr:
        temp = k - i
        if temp in s:
            return (temp, i)
        s.add(i)
    return -1

arr = list(map(int, input().split()))
k = int(input())
s = set()

print(getPair(arr, k))