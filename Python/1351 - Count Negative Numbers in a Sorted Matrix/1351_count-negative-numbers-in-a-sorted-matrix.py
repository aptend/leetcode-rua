from leezy import solution, Solution


class Q1351(Solution):
    @solution
    def countNegatives(self, grid):
        # O(m + n)
        # binary search m*log(n)
        m, n = len(grid), len(grid[0])
        i, j = 0, n-1
        ans = 0
        while i < m and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                ans += m - i
                j -= 1
        return ans


def main():
    q = Q1351()
    q.add_case(q.case([[4, 3, 2, -1],
                       [3, 2, 1, -1],
                       [1, 1, -1, -2],
                       [-1, -1, -2, -3]]).assert_equal(8))
    q.add_case(q.case([[-1]]).assert_equal(1))
    q.add_case(q.case([[1, -1], [-1, -1]]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
