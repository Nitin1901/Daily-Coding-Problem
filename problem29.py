def encode(s):
    r = ''
    x = 1
    l = len(s)
    for i in range(1, l):
        if s[i] != s[i-1]:
            r += str(x) + s[i-1]
            x = 1
        else:
            x += 1
    r += str(x) + s[l-1]
    return r

s = input("Enter the string: ")
print(encode(s))