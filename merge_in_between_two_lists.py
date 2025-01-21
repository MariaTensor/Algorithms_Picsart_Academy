def mergeInBetween(self, list1, a, b, list2):
        tmp = list1
        tmp2 = list1
        last = tmp2
        for i in range(b+1):
            tmp2 = tmp2.next
        for i in range(a-1):
            tmp = tmp.next
        tmp.next = list2
        while tmp.next:
            tmp = tmp.next
        tmp.next = tmp2
        return last
