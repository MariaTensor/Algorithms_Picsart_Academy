class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def search(self,key):
        current = self.head
        position = 0
        while current:
            if key == current.data:
                return position
            current = current.next
            position += 1
        return -1
    
    def length(self):
        current = self.head
        temp = 0
        while current:
            temp += 1
            current = current.next
        return temp
    
    def insert_at_beginning(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,value):
        current = self.head
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self,position,value):
        new_node = Node(value)
        if position == 0:
            self.insert_at_beginning(value)
            return
        current = self.head
        for i in range(position):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_from_beg(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
    
    def delete_by_value(self,value):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print(f"Node with value {value} was not found.")

    
    def getMiddleElement(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def hasCycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def reverse(self,head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def delete_node(self,node):
        node.data = node.next.data
        node.next = node.next.next
    
    def display(self):
        elements = self.traverse()
        print(elements)

def mergeTwoLists(list1, list2):
    dummy = LinkedList()
    tmp = dummy
    while list1 and list2:
        if list1.data < list2.data:
            print(list1.data)
            tmp.next = list1
            list1 = list1.next
        else:
            tmp.next = list2
            list2 = list2.next
        tmp = tmp.next
    if list1:
        tmp.next = list1
    if list2:
        tmp.next = list2
    return dummy.next

def getDecimalValue(head):
    a = []
    while head:
        a.append(head.data)
        head = head.next
    res = 0
    for i in range(len(a)):
        res += pow(2,i) * a[len(a)-i-1]
    return res

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
# ll.display() 

ll.insert_at_beginning(5)
# ll.display()

ll.insert_at_position(2, 15)
# ll.display()

l2 = LinkedList()
l2.insert_at_end(15)
l2.insert_at_end(25)
l2.insert_at_end(35)

# print("Length:", ll.length()) 

# print("Search for 20:", ll.search(20))
# print("Search for 50:", ll.search(50))

ll.delete_from_beg()
# ll.display()

ll.delete_from_end()
# ll.display() 

ll.delete_by_value(15)
# ll.display()

ll.delete_by_value(100) 
ll.insert_at_end(100)
ll.insert_at_end(200)
ll.insert_at_beginning(4)
ll.insert_at_position(3, 15)
# ll.display()
# ll.reverse(ll.head)
# ll.display()

# print("Middle element:", ll.getMiddleElement(ll.head))
ll.display()
l2.display()
a = mergeTwoLists(ll.head,l2.head)
print("Merged List:")
ll3 = LinkedList()
ll3.head = a
ll3.display()