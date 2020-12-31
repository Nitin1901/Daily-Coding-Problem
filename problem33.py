class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    root = None
    number = 0

    def insertNode(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            cur = self.root
            prev = None
            while cur:
                prev = cur
                if value <= cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
            if value <= prev.value:
                prev.left = Node(value)
            else:
                prev.right = Node(value)
        self.number += 1

    def printTree(self, node):
        if self.root == None:
            print('Empty tree')
        else:
            if node == None:
                return
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)

    def getMedian(self):
        if self.number == 0:
            return 0
        if self.number == 1:
            return self.root.value
        req = (self.number//2)
        if self.number%2 == 1:
            return self.getValue(self.root, req+1)
        elif self.number%2 == 0:
            return (self.getValue(self.root, req)+self.getValue(self.root, req+1))/2

t = Tree()
x = [2,1,5,7,2,0,5]

for i in x:
    t.insertNode(i)
    print(t.getMedian())