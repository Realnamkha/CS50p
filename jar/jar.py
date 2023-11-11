class Jar:
    size = 0
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = Jar.size


    # def __str__(self):
    #     return f"{self.name}"

    def deposit(self, n):
        self.size = Jar.size
        total = self.size + n
        if (total<=self.capacity):
            Jar.size = total


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
    try:
        namkha = Jar(-1)
        print(namkha.capacity)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
