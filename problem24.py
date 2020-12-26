class Node:
    def __init__(self, data, is_locked=False):
        self.data = data
        self.left = None
        self.right = None
        self.is_locked = is_locked

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4, True)
root.left.right = Node(5)

def isLocked(node, data):
    if node == None:
        return None
    if node.data == data:
        return node.is_locked
    result = isLocked(node.left, data)
    if result is not None:
        return result
    result = isLocked(node.right, data)
    if result is not None:
        return result

def checkChildLocks(node):
    if node == None:
        return True
    if node.is_locked == True:
        return False
    if checkChildLocks(node.left) and checkChildLocks(node.right):
        return True
    return False

def lock(node, data):
    if node == None:
        return None 
    if node.data == data:
        if checkChildLocks(node.left) and checkChildLocks(node.right):
            node.is_locked = True
            return True
        return False
    result = lock(node.left, data)
    if result is not None:
        return result
    result = lock(node.right, data)
    if result is not None:
        return result
    
def unlock(node, data):
    if node == None:
        return None
    if node.data == data:
        if checkChildLocks(node.left) and checkChildLocks(node.right):
            node.is_locked = False
            return True
        return False
    result = unlock(node.left, data)
    if result is not None:
        return result
    result = unlock(node.right, data)
    if result is not None:
        return result

print(isLocked(root, 4))
print(unlock(root, 4))
print(isLocked(root, 4))

print(lock(root, 4))
print(isLocked(root, 4))