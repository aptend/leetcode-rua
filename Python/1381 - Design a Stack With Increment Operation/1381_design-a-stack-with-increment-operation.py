class CustomStack:

    def __init__(self, maxSize: int):
        self.N = maxSize
        self.log = [0] * self.N
        self.stack = []
        self.base = 0
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.N:
            if self.size > 0:
                self.log[self.size-1] += self.base
            self.base = 0
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            self.base += self.log[self.size-1]
            self.log[self.size-1] = 0
            self.size -= 1
            return self.base + self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k <= 0 or self.size <= 0:
            return
        k = min(k, self.size)
        self.log[k-1] += val

def main():
    customstack = CustomStack(3)
    operations = ['push', 'push', 'pop', 'push', 'push', 'push', 'increment', 'increment', 'pop', 'pop', 'pop', 'pop']
    oprands = [[1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(customstack, opt):
            print(getattr(customstack, opt).__call__(*opd))


if __name__ == '__main__':
    main()
