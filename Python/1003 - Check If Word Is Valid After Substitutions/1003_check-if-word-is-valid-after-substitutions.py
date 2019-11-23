from leezy import solution, Solution


class Q1003(Solution):
    @solution
    def isValid(self, S):
        # 52ms 68.34%
        stack = []
        for x in S:
            if x == 'a':
                stack.append('a')
            elif x == 'b':
                if not stack or stack[-1] != 'a':
                    return False
                stack.pop()
                stack.append('b')
            else:
                if not stack or stack[-1] != 'b':
                    return False
                stack.pop()
        return not stack


def main():
    q = Q1003()
    q.add_case(q.case('aabcbc'))
    q.run()

if __name__ == '__main__':
    main()
