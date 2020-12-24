import time

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# DFS
def traverse(x):
    if x == None:
        return 
    traverse(x.left)
    print(x.data)
    traverse(x.right)

# Approach 1
def check(x):
    if x == None:
        return 1
    if x.left and x.right:
        if x.left.data != x.data or x.right.data != x.data:
            return 0
    if check(x.left) and check(x.right):
        return 1

def unival(x):
    if x == None:
        return 0
    return check(x) + unival(x.left) + unival(x.right)

# Approach 2
def count_unival(x):
    cnt, is_unival = helper(x)
    return cnt

def helper(x):
    if x == None:
        return (0, True)
    left_cnt, left_check = helper(x.left)
    right_cnt, right_check = helper(x.right)
    is_unival = True
    if (not left_check) or (not right_check):
        is_unival = False
    if (x.left) and (x.left.data != x.data):
        is_unival = False
    if (x.right) and (x.right.data != x.data):
        is_unival = False
    if is_unival:
        return (left_cnt + right_cnt + 1, True)
    else:
        return (left_cnt + right_cnt, False)

head = Node(0)
head.left = Node(1)
head.right = Node(0)
head.right.left = Node(1)
head.right.left.left = Node(1)
head.right.left.right = Node(1)
head.right.right = Node(0)
head.left.left = Node(0)
head.left.right = Node(1)
head.left.left.left = Node(1)
head.left.left.right = Node(0)
head.left.left.right.left = Node(0)
head.left.left.right.right = Node(0)

#traverse(head)
start = time.time()
print(unival(head))
end = time.time()
print(f'Approach 1 = {1000*(end-start)}ms')
start = time.time()
print(count_unival(head))
end = time.time()
print(f'Approach 2 = {1000*(end-start)}ms')