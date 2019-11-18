from leezy import Solution, solution
import math


class Q996(Solution):
    @solution
    def numSquarefulPerms(self, A):
        # 20ms 75.70%
        self.ans = 0
        used = [False] * len(A)
        A = sorted(A)
        self.dfs(A, 0, used, None)
        return self.ans

    def is_squareful(self, x, y):
        s = int(math.sqrt(x+y))
        return s*s == x+y

    def dfs(self, A, depth, used, prev):
        if depth == len(A):
            self.ans += 1
            return
        prev_tried = -1
        for i in range(len(A)):
            if used[i] or A[i] == prev_tried:
                continue
            if prev is not None and not self.is_squareful(prev, A[i]):
                continue
            used[i] = True
            prev_tried = A[i]
            self.dfs(A, depth+1, used, A[i])
            used[i] = False


def main():
    q = Q996()
    q.add_case(q.case([1, 17, 8]).assert_equal(2))
    q.add_case(q.case([2, 2, 2]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
