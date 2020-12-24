class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" "),
        if self.right:
            self.right.PrintTree()

def serialize(t):
    if t == None:
        return "X"
    return f"{t.data} {serialize(t.left)} {serialize(t.right)}"

def deserialize(temp, arr):
    if arr == []:
        return
    a = arr.pop(0)
    if a == "X":
        return
    else:
        temp = Node(a)
        temp.left = deserialize(temp.left, arr)
        temp.right = deserialize(temp.right, arr)
        return temp

t = Node("3")
t.left = Node("5")
t.left.left = Node("1")
t.right = Node("1")
t.right.left = Node("2")
t.right.left.left = Node("3")
t.right.left.right = Node("6")
print('Original Tree = ', end="")
t.PrintTree()
print()
s = serialize(t)
print(f'Serialized = {s}')
arr = s.split()
a = arr.pop(0)
d = Node(a)
d.left = deserialize(d.left, arr)
d.right = deserialize(d.right, arr)
print('Deserialized = ', end="")
d.PrintTree()
print()