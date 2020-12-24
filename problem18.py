arr = list(map(int, input().split()))
k = int(input())
l = len(arr)

def search(arr, k, i):
    return max(arr[i: i+k])

for i in range(l-k+1):
    print(search(arr, k, i))