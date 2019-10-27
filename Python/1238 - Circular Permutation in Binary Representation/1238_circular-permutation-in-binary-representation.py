from leeyzer import solution, Solution

from collections import deque

class Q1238(Solution):
    @solution
    def circularPermutation(self, n, start):
        # 268ms 14.29%
        # it is a bit slow, but it is intuitive
        # 89. gray code
        # it is unfair for 'gray code' to receive so many dislikes
        ans = deque()
        ans.append(0)
        for i in range(0, n):
            base = 2 ** i
            for j in reversed(range(0, len(ans))):
                ans.append(base + ans[j])
        # ans[0] and ans[-1] differ by only one bit
        # rotate it
        while ans[0] != start:
            ans.rotate(-1)
        return ans



def main():
    q = Q1238()
    q.add_args(2, 3)
    q.run()

if __name__ == '__main__':
    main()
