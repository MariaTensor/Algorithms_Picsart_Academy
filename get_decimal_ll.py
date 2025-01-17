def get_decimal(head):
    res = 0
    while head:
        res = 2* res + head.val
        head = head.next
    return res