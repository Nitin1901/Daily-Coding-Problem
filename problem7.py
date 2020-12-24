def encoding(s, k, store):
    if k == 0:
        return 1
    if s[-k] == '0':
        return 0
    if store[k]!=None:
        return store[k]
    result = encoding(s, k-1, store)
    if k > 1 and int(s[-k: -k+1]) < 27:
        result += encoding(s, k-2, store)
    store[k] = result
    return result

s = input("Enter the encoding: ")
k = len(s)
store = [None]*(k+1)
print(encoding(s, k, store))