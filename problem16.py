arr = []

def record(arr, data, n):
    l = len(arr)
    if l == n:
        arr.remove(arr[0])
    arr.append(data)
    return

def get_last(arr, i):
    if arr == []:
        print("No data.")
        return
    print(f"Last {i}th record = {arr[-i]}")
    return

n = int(input("Enter the size of the array: "))
print("1.Add a record.")
print("2.Get the last n records.")
print("3.Quit.")
ch = int(input("Enter your choice: "))
while(ch != 3):
    if ch == 1:
        data = int(input("Enter the data: "))
        record(arr, data, n)
    elif ch == 2:
        i = int(input("Enter the last ith record to retrieve: "))
        get_last(arr, i)
    else:
        print("Wrong input.")
    ch = int(input("Enter your choice: "))
