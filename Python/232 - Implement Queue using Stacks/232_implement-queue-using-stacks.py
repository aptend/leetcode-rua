
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.dump = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.dump.append(self.stack.pop())
        self.stack.append(x)
        while self.dump:
            self.stack.append(self.dump.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


class MyQueue2:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def _shift(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def pop(self) -> int:
        self._shift()
        return self.outstack.pop()

    def peek(self) -> int:
        self._shift()
        return self.outstack[-1]

    def empty(self) -> bool:
        return len(self.instack) == 0 and len(self.outstack) == 0



def main():
    myqueue = MyQueue()
    operations = ['push', 'push', 'peek', 'pop', 'empty']
    oprands = [[1], [2], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(myqueue, opt):
            print(getattr(myqueue, opt).__call__(*opd))


if __name__ == '__main__':
    main()
