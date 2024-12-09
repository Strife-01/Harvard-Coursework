class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "\U0001F36A" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too not enough space in the jar")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Capacity is not a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size

    def __del__(self):
        print("This \U0001F36A jar has been broken! ...")
