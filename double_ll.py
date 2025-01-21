class Node:
    def __init__(self,val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
def forward_traversal(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
def backward_traversal(tail):
    curr = tail
    while curr:
        print(curr.val)
        curr = curr.prev
def size(head):
    count = 0
    curr = head
    while curr:
        count +=1
        curr = curr.next
    return count
def insertBegin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def insertEnd(head,data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head
def insert_at_pos(head,pos,new_data):
    new_node = Node(new_data)
    if pos == 0:
        return insertBegin(head,new_data)
    curr = head
    for i in range(pos - 1):
        if curr is None:
            print("Position is out of bonds")
            return head
        curr = curr.next
    if curr is None:
        print("Position is out of bounds.")
        return head
    if curr.next is None:
        curr.next = new_node
        new_node.prev = curr
    else:
        tmp = curr.next
        curr.next = new_node
        new_node.next = tmp
        new_node.prev = curr
        tmp.prev = new_node
    return head
def deleteBeg(head):
    if head is None:
        print("empty")
        return None
    tmp = head
    head = head.next
    if head is not None:
        head.prev = None
    del tmp
    return head
def deleteEnd(head):
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def delete_by_pos(head,pos):
    if head is None:
        return None
    if pos == 0:
        return deleteBeg(head)
    curr = head
    for i in range(pos - 1):
        if  curr is None or curr.next is None:
            print("Out of bounds")
            return head
        curr = curr.next
    if curr.next is None:
        print("Out of bounds")
        return head
    tmp = curr.next.next
    if tmp:
        tmp.prev = curr
    curr.next = tmp
    return head

def delete_by_val(head,val):
    if head is None:
        return None
    if head.val == val:
        return deleteBeg(head)
    curr = head
    while curr:
        if curr.next.val == val:
            break
        curr = curr.next
    if curr is None or curr.next is None:
        print("Value not found in the list.")
        return head
    
    tmp = curr.next.next
    if tmp:
        tmp.prev = curr
    curr.next = tmp
    return head
    

    




head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)
fifth = Node(5)
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = forth
forth.prev = third
forth.next = fifth
fifth.prev = forth
first = insertBegin(head,110)
last = insertEnd(first,220)
insert_at_pos(first,3,555)
dele = deleteBeg(first)
a = delete_by_pos(first,4)
forward_traversal(a)
