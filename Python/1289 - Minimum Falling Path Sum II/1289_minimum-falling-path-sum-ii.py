from leezy import solution, Solution


class Q1289(Solution):
    @solution
    def minFallingPathSum(self, arr):
        N = len(arr)
        if N <= 1:
            return None
        dp = [0] * N
        for row in arr:
            n1 = n2 = (float('inf'), -1)
            for j, x in enumerate(dp):
                if x <= n1[0]:
                    n2 = n1
                    n1 = (x, j)
                elif x < n2[0]:
                    n2 = (x, j)

            for i in range(N):
                best_choice = n2[0] if i == n1[1] else n1[0]
                dp[i] = row[i] + best_choice
        return min(dp)


def main():
    q = Q1289()
    q.add_case(q.case([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).assert_equal(13))
    q.run()

if __name__ == '__main__':
    main()
