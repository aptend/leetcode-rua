from leezy import Solution, solution
import math

class Q996(Solution):
    @solution
    def numSquarefulPerms(self, A):
        """20ms beats 75.70%
        """
        ans = [0]
        used = [False] * len(A)
        A = sorted(A)
        self.dfs(A, 0, used, None, ans)
        return ans[0]

    def is_squareful(self, x, y):
        s = int(math.sqrt(x+y))
        return s*s == x+y

    def dfs(self, A, depth, used, prev, ans):
        if depth == len(A):
            ans[0] += 1
            return
        prev_tried = -1
        for i in range(len(A)):
            if used[i] or A[i] == prev_tried:
                continue
            if prev is not None and not self.is_squareful(prev, A[i]):
                continue
            used[i] = True
            prev_tried = A[i]
            self.dfs(A, depth+1, used, A[i], ans)
            used[i] = False


def main():
    q = Q996()
    q.add_args([3])  # 1
    q.add_args([0, 3])  # 0
    q.add_args([1, 17, 8])
    q.add_args([2, 2, 7])
    q.run()


if __name__ == "__main__":
    main()
