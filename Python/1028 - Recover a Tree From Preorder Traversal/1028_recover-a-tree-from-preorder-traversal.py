from leezy import solution, Solution
from leezy.assists import TreeNode


class Parser:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.N = len(s)

    def next_int(self):
        i, N = self.i, self.N
        if i == N:
            return None
        num = ''
        while i < N and self.s[i] != '-':
            num += self.s[i]
            i += 1
        self.i = i
        return int(num) if num else 0

    def next_slug_cnt(self):
        i, N = self.i, self.N
        if i == N:
            return None
        cnt = 0
        while i < N and self.s[i] == '-':
            cnt += 1
            i += 1
        self.i = i
        return cnt


class Q1028(Solution):
    @solution
    def recoverFromPreorder(self, S):
        # 80ms 61.19%
        if not S:
            return None
        parser = Parser(S)

        stack = [(TreeNode(parser.next_int()), 0)]
        while True:
            slug_cnt = parser.next_slug_cnt()
            if slug_cnt is None:
                break
            val = parser.next_int()
            node = TreeNode(val)
            while stack[-1][1] > slug_cnt:
                stack.pop()
            if stack[-1][1] == slug_cnt:
                stack.pop()
                stack[-1][0].right = node
            else:
                stack[-1][0].left = node
            stack.append((node, slug_cnt))
        return stack[0][0]


def main():
    q = Q1028()
    q.add_case(q.case('1-2--3--4-5--6--7')
                .assert_true_with(
                    lambda x: str(x) == str(TreeNode.make_tree([1, 2, 5, 3, 4, 6, 7]))))
    q.add_case(q.case('1-401--349---90--88')
                .assert_true_with(
                    lambda x: str(x) == str(TreeNode.make_tree([1, 401, None, 349, 88, 90]))))
    q.run()


if __name__ == '__main__':
    main()
