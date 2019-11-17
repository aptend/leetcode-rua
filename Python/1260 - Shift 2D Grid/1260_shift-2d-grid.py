from leezy import solution, Solution
from collections import deque
from itertools import chain


class Q1260(Solution):
    @solution
    def shiftGrid(self, grid, k):
        # 172ms
        # O(mn) time / O(1) space
        n, m = len(grid), len(grid[0])
        k = k % (n * m)

        di, dj = divmod(k, m)

        def shift(si, sj):
            i, j = si, sj
            prev = grid[i][j]
            while True:
                carry, nj = divmod(j+dj, m)
                ni = (i + di + carry) % n
                cur = grid[ni][nj]
                grid[ni][nj] = prev
                prev = cur
                i, j = ni, nj
                if i == si and j == sj:
                    break

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for x in range(gcd(k, n*m)):
            si, sj = divmod(x, m)
            shift(si, sj)
        return grid

    @solution
    def shift_grid(self, grid, k):
        # 172ms
        # O(mn) time / O(mn) space
        flatten = deque(chain.from_iterable(grid))
        flatten.rotate(k)
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                grid[i][j] = flatten[i*m+j]
        return grid


def main():
    q = Q1260()
    q.add_case(q.case([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
    q.run()


if __name__ == '__main__':
    main()
