class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def remove_nth_node(head,n):
    dummy = Node()
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(n+1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

def display(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    

#example usage
head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
res = remove_nth_node(head, 1)
display(res)
    