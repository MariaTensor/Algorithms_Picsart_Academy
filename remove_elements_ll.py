class ListNode():
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
def remove_element(head,val):
    prev = ListNode()
    dummy = prev
    tmp = head
    if head is None:
        return head
    while tmp:
        if tmp.val != val:
            prev.next = tmp
            prev = prev.next
        tmp = tmp.next
        prev.next = None
    return dummy.next