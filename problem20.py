class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def reverse(self):
        before = None
        cur = self.head
        while cur:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        self.head = before

    def print_list(self):
        cur = self.head
        while cur.next:
            print(cur.data, end="->")
            cur = cur.next
        print(cur.data)

A = LinkedList()
A.add(3)
A.add(7)
A.add(8)
A.add(10)

B = LinkedList()
B.add(99)
B.add(1)
B.add(8)
B.add(10)

def findIntersectingNode(A, B):
    A.reverse()
    B.reverse()
    temp = -1
    head1 = A.head
    head2 = B.head
    while head1.data == head2.data:
        temp = head1.data
        head1 = head1.next
        head2 = head2.next
    return temp

print(findIntersectingNode(A, B))