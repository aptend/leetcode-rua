from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        size = len(self.q)
        self.q.append(x)
        for _ in range(size):
            head = self.q.popleft()
            self.q.append(head)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0


def main():
    mystack = MyStack()
    operations = ['push', 'push', 'top', 'pop', 'empty']
    oprands = [[1], [2], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(mystack, opt):
            print(getattr(mystack, opt).__call__(*opd))


if __name__ == '__main__':
    main()
