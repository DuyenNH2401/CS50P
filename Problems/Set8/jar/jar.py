class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError
        if n + self.size > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if self.size - n < 0:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()  # Tạo một thể hiện của lớp Jar
    jar.deposit(5)
    print(jar)  # In ra số lượng cookie
    jar.withdraw(2)
    print(jar)
    print(f"Capacity: {jar.capacity}, Size: {jar.size}")

if __name__ == '__main__':
    main()