from leezy import solution, Solution


class Q946(Solution):
    @solution
    def validateStackSequences(self, pushed, popped):
        # 88ms
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped = popped[1:]
        return len(stack) == 0

    @solution
    def validate_stack_seq(self, pushed, popped):
        # 72ms
        stack = []
        popped.reverse()
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return len(stack) == 0


def main():
    q = Q946()
    q.add_case(q.case([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    q.add_case(q.case([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    q.run()

if __name__ == '__main__':
    main()
