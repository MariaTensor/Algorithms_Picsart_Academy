class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.deque.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the item from the front of the deque."""
        if not self.is_empty():
            return self.deque.pop(0)
        else:
            return "Deque is empty"

    def remove_rear(self):
        """Remove and return the item from the rear of the deque."""
        if not self.is_empty():
            return self.deque.pop()
        else:
            return "Deque is empty"

    def size(self):
        return len(self.deque)

    def front(self):
        """Return the item at the front without removing it."""
        if not self.is_empty():
            return self.deque[0]
        else:
            return "Deque is empty"

    def rear(self):
        """Return the item at the rear without removing it."""
        if not self.is_empty():
            return self.deque[-1]
        else:
            return "Deque is empty"


# Example usage
dq = Deque()

# Add elements
dq.add_front(10)
dq.add_rear(20)
dq.add_front(5)
print("Deque after additions:", dq.deque)  # Output: [5, 10, 20]

# Remove elements
print("Removed from front:", dq.remove_front())  # Output: 5
print("Removed from rear:", dq.remove_rear())    # Output: 20
print("Deque after removals:", dq.deque)         # Output: [10]

# Check size and front/rear
print("Size of deque:", dq.size())               # Output: 1
print("Front of deque:", dq.front())             # Output: 10
print("Rear of deque:", dq.rear())               # Output: 10
