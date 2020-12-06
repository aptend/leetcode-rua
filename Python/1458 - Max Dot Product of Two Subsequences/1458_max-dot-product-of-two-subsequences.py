from leezy import solution, Solution


class Q1458(Solution):
    @solution
    def maxDotProduct(self, nums1, nums2):
        N1, N2 = len(nums1), len(nums2)
        MIN = float('-inf')
        dp = [[MIN for _ in range(N2+1)] for _ in range(N1+1)]
        for i in range(1, N1+1):
            for j in range(1, N2+1):
                dp[i][j] = max(
                    nums1[i-1]*nums2[j-1],
                    dp[i-1][j-1] + nums1[i-1]*nums2[j-1],
                    dp[i-1][j],
                    dp[i][j-1],
                )
        return dp[N1][N2]


def main():
    q = Q1458()
    q.add_case(q.case([2, 1, -2, 5], [3, 0, -6]).assert_equal(18))
    q.add_case(q.case([-1, -1], [1, 1]).assert_equal(-1))
    q.add_case(q.case(
        [-3, -8, 3, -10, 1, 3, 9],
        [9, 2, 3, 7, -9, 1, -8, 5, -1, -1]).assert_equal(200))
    q.run()


if __name__ == '__main__':
    main()
