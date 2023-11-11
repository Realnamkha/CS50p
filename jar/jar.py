class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    # def __str__(self):
    #     return f"{self.name}"

    def deposit(self, n):
        self._size = int(self._size) + n
        if (total<=self.capacity):
            return self._size
        else:
            raise ValueError("Capacity Exceeded")


    def withdraw(self, n):
        ...

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
        print(namkha.deposit(10))
        print(namkha.capacity)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
