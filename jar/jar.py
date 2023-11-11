class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

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
        ...

def main():
    namkha = Jar(-1)
    print(namkha.capacity)



if __name__ == "__main__":
    main()
