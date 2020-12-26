words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = 'bedbathandbeyond'

def getList(words, string, out):
    if not string:
        return out
    for i in range(1, len(string)+1):
        prefix = string[:i]
        if prefix in words:
            out.append(prefix)
            return getList(words, string[i:], out)

print(getList(words, string, []))