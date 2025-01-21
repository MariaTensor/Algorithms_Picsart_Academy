def swapNodes(head, k):
    tmp = head
    last = head
    size = head
    count = 0
    while size:
        count += 1
        size = size.next
    for i in range(k - 1):
        tmp = tmp.next
    for i in range(count - k):
        last = last.next
    tmp.val,last.val = last.val,tmp.val
    return head


def swapNodes(head,k):
    first = head
    last = head
    for i in range(1,k):
        first = first.next
    null_checker = first
    while null_checker.next:
        last = last.next
        null_checker = null_checker.next
    last.val,first.val = first.val, last.val
    return head