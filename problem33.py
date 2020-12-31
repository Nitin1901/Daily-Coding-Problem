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

    def printTreeInorder(self, node, c, n): 
        if self.root == None: 
            return 
        else: 
            if node == None or c[0] > n: 
                return
            self.printTreeInorder(node.left, c, n) 
            c[0] += 1 
            if c[0] == n: 
                print(node.value)
                return node.value
            self.printTreeInorder(node.right, c, n) 
                
    def printTree(self, node, n): 
        c = [0] 
        self.printTreeInorder(node, c, n)

    def getMedian(self):
        if self.number == 0:
            return 0
        if self.number == 1:
            return self.root.value
        req = (self.number//2)
        if self.number%2 == 1:
            return self.printTree(self.root, req+1)
        elif self.number%2 == 0:
            return (self.printTree(self.root, req)+self.printTree(self.root, req+1))/2

t = Tree()
x = [2,1,5,7,2,0,5]

for i in x:
    t.insertNode(i)
    print(t.getMedian())
