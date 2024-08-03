''' Day 14: Iterators

        Task 1: Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.

        Task 2: The iterator should stop when it reaches a limit defined in the constructor. '''


class Fibonacci:
    def __init__(self, limit):
        self.current = 0
        self.next = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        current_value = self.current
        self.current, self.next = self.next, self.current + self.next
        return current_value


if __name__ == '__main__':
    fib = Fibonacci(10)
    for i in fib:
        print(i)
