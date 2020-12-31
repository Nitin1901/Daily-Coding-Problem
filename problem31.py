def minEditDistance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 0:
        return l2
    if l2 == 0:
        return l1
    print(l1, l2)
    table = [[0 for c in range(l1+1)] for r in range(l2+1)]
    for i in range(l1+1):
        table[0][i] = i
    for i in range(l2+1):
        table[i][0] = i
    for r in range(1, l2+1):
        for c in range(1, l1+1):
            if s2[r-1] == s1[c-1]:
                table[r][c] = table[r-1][c-1]
            else:
                table[r][c] = 1 + min(table[r-1][c], table[r][c-1], table[r-1][c-1])
    for r in range(l2+1):
        for c in range(l1+1):
            print(table[r][c], end=" ")
        print()
    print('Minimum edits =', table[-1][-1])

minEditDistance('abcdef', 'azced')