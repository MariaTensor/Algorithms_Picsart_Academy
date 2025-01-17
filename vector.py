class Vector:
    def __init__(self):
        self._capacity = 0
        self._size = 0
        self.vector = []
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        self._capacity = value
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value
    
    def is_empty(self):
        return not self.size
    
    def resize(self):
        if not self.capacity:
            self.capacity = 2
        else:
            self.capacity *= 2
        self.vector.extend([0] * (self.capacity - self.size))
    
    def push_back(self, value):
        if self.size == self.capacity:
            self.resize()
        self.vector[self.size] = value
        self.size += 1
    
    def pop_back(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty vector")
        self.size -= 1
        return self.vector.pop()
    
    def shrink_to_fit(self):
        if self.size == self.capacity:
            return
        self.vector = self.vector[:self.size]
        self.capacity = self.size
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        if self.size == self.capacity:
            self.resize()
        self.vector = self.vector[:index] + [value] + self.vector[index:self.size]
        self.size += 1
    
    def __repr__(self):
        return f"Vector({self.vector[:self.size]})"


vec = Vector()
vec.push_back(1)
vec.push_back(2)
vec.push_back(3)
print(vec)
vec.pop_back()
vec.insert(0,765)
print(vec)
vec.resize()
print(vec.size, vec.capacity)

