class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
def oddEvenList(self, head) :
    if head is None:
        return head
    tmp = head
    dummy = head
    odd = dummy
    prev = ListNode(0)
    even = prev
    while tmp and tmp.next:
        tmp = tmp.next
        prev.next = tmp
        prev = prev.next
        dummy.next = tmp.next
        tmp = tmp.next
        dummy = dummy.next
    prev.next = None
    even = even.next
    res = odd
    while odd.next:
        odd = odd.next
    odd.next = even
    return res

def odd_even(self,head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
    