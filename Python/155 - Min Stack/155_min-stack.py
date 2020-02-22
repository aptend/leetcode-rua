
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minv = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minv or self.minv[-1] > x:
            self.minv.append(x)
        else:
            self.minv.append(self.minv[-1])

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.minv.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minv:
            return self.minv[-1]


def main():
    minstack = MinStack()
    operations = ['push', 'push', 'push', 'getMin', 'pop', 'top', 'getMin']
    oprands = [[-2], [0], [-3], [], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(minstack, opt):
            print(getattr(minstack, opt).__call__(*opd))


if __name__ == '__main__':
    main()
