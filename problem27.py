brackets = input("Enter the sequence: ")

def getClosing(b):
    if b == '(':
        return ')'
    elif b == '{':
        return '}'
    elif b == '[':
        return ']'

def isBalanced(brackets):
    if not brackets:
        return True
    l = len(brackets)
    if l%2 == 1:
        print("Length is not even")
        return False
    stack = []
    for i in range(l):
        if brackets[i] in ['{', '[', '(']:
            stack.append(brackets[i])
        else:
            if getClosing(stack.pop()) != brackets[i]:
                print("Not matching")
                return False
    if stack == []:
        return True
    return False

print(isBalanced(brackets))
