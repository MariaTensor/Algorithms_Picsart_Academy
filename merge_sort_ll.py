class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getMiddle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeLists(l1,l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

def mergesort(head):
    mid = getMiddle(head)
    right = mid.next
    mid.next = None
    return mergeLists(mergesort(right),mergesort(head))



