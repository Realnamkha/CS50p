class Jar:
    size = 0
    def __init__(self, capacity=12):
        self.capacity = capacity


    # def __str__(self):
    #     return f"{self.name}"

    def deposit(self, n):
        self.x = Jar.size
        total = self.x + n
        if (total<=self.capacity):
            Jar.size = total
            return Jar.size
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
        ...

def main():
    try:
        namkha = Jar(30)
        print(namkha.deposit(10))
        print(namkha.capacity)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
