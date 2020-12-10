from leezy import solution, Solution

import numpy as np

class Q1478(Solution):
    @solution
    def minDistance(self, houses, k):
        # 516ms 75%
        memo = {}
        houses = sorted(houses)
        def dist(i, j, k):
            if i == j or j - i + 1 <= k:
                return 0

            key = (i, j, k)
            if key in memo:
                return memo[key]

            if k == 1:
                ans = 0
                while i < j:
                    ans += houses[j] - houses[i]
                    i += 1
                    j -= 1
            else:
                ans = float('inf')
                for split in range(i, j):
                    ans = min(ans, dist(i, split, 1) + dist(split+1, j, k-1))
            memo[key] = ans
            return ans
        return dist(0, len(houses)-1, k)


def main():
    q = Q1478()
    q.add_case(q.case([1, 4, 8, 10, 20], 3).assert_equal(5))
    q.add_case(q.case([2, 3, 5, 12, 18], 2).assert_equal(9))
    q.add_case(q.case([7, 4, 6, 1], 1).assert_equal(8))
    q.add_case(q.case([3, 6, 14, 10], 4).assert_equal(0))
    q.add_case(q.case([19, 28, 10, 30, 11, 6, 5, 17], 4).assert_equal(6))
    q.run()


if __name__ == '__main__':
    main()
