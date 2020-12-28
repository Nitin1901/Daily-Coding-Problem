class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNode(head, data):
    if head == None:
        head = Node(data)
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
    return head

def printList(head):
    if head == None:
        print("The list is empty")
    else:
        cur = head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

def getLength(head):
    l = 0
    cur = head
    while cur:
        l += 1
        cur = cur.next
    return l

def deleteFromLast(head, k):
    if head == None:
        return None
    l = getLength(head)
    if not 1 <= k <= l:
        return head
    if k == l:
        head = head.next
    else:
        cur = head
        prev = None
        for i in range(l-k):
            prev = cur
            cur = cur.next
        prev.next = cur.next
    return head

head = None
head = insertNode(head, 1)
head = insertNode(head, 2)
head = insertNode(head, 3)
head = deleteFromLast(head, 2)
printList(head)
