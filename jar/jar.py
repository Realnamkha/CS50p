class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
         return '🍪' * self._size

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
            return self._size
        else:
            raise ValueError("Capacity Exceeded")


    def withdraw(self, n):
        if self._size >= 0:
            self._size -= n
            return self._size
        else:
            raise ValueError("No cookies left")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity)>=0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid Capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError("Invalid Size")

def main():
    try:
        namkha = Jar(30)
        print(namkha.capacity)
        print(namkha.deposit(20))
        print(namkha.withdraw(15))
        print(namkha.size)
        print(namkha)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
