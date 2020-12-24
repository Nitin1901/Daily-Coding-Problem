import random
import time

# Approach 1
def getNumber(arr):
    count = dict()
    m = max(arr)
    for i in range(1, m+1):
        count[i] = 0
    for i in arr:
        if i>0:
            if count[i] == 0:
                count[i] += 1
    for k, v in count.items():
        if v == 0:
            return k
    return m+1

# Approach 2
def alternate(arr):
    n = len(arr)
    for i in range(n):
        correctPos = arr[i]-1 
        while 1 <= arr[i] <= n and arr[i] != arr[correctPos]:
            arr[i], arr[correctPos] = arr[correctPos], arr[i]
            correctPos = arr[i]-1 
    for i in range(n):
        if i+1 != arr[i]:
            return i+1
    return n+1

"""
1000 <= N <= 10000
-1000 <= A[i] <= 1000
"""
tc = int(input("Enter the number of test cases: "))
print('{0: <10} | {1: <10} | {2: <10}'.format('Length', 'Approach 1', 'Approach 2'))

for _ in range(tc):
    
    arr = [(random.randint(-1000, 1000)) for _ in range(random.randint(1000, 10000))]

    tic1 = time.time()
    approach1 = getNumber(arr)
    tac1 = time.time()

    tic2 = time.time()
    approach2 = alternate(arr)
    tac2 = time.time()

    if approach1 == approach2:  
        print('{0: <10} | {1: 10.4f} | {2: 10.4f}'.format(str(len(arr)), 1000*(tac1-tic1), 1000*(tac2-tic2)))
    else:
        print(f'############## The test case failed ##############')
        print(approach1)
        print(approach2)
