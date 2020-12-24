def over(alphabets, k):
    l = 0
    for _, v in alphabets.items():
        if v > 0:
            l += 1
        if l > k:
            return 1
    return 0

def longestSequence(s, k):
    start, end, windowSize, windowStart = 0, 0, 1, 0
    alphabets = {}
    for i in s:
        if i not in alphabets:
            alphabets[i] = 1
        else:
            alphabets[i] += 1
        end += 1
        while over(alphabets, k):
            print("crossed")
            alphabets[s[start]] -= 1
            start += 1
        if end-start+1 > windowSize:
            windowSize = end-start+1
            windowStart = start
    return s[windowStart: windowStart+windowSize-1]
    
s = input("Enter the string: ")
k = int(input("Enter k: "))
print(longestSequence(s, k))