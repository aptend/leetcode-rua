from leeyzer import solution, Solution
from pprint import pprint
class Q1035(Solution):
    @solution
    def maxUncrossedLines(self, A, B):
        # 200ms 81.82%
        # same with longest common subsequences
        M, N = len(A), len(B)
        # dp[m][n] means how many lines at most when using A[m:] and B[n:]
        dp = [[0] * (N+1) for _ in range(M+1)]
        for m in range(M-1, -1, -1):
            for n in range(N-1, -1, -1):
                # if A = [1, 4, 4] and B = [1, 2, 4] and answer is 3
                # we can solve it by changing a little:
                # dp[m][n] = max(dp[m+1][n], dp[m][n+1]) + int(A[m] == B[n])
                dp[m][n] = max(dp[m][n+1], dp[m+1][n])
                if A[m] == B[n]:
                    dp[m][n] = max(dp[m+1][n+1]+1, dp[m][n])
        return dp[0][0]


def main():
    q = Q1035()
    q.add_args([1, 4, 2], [1, 2, 4])
    q.add_args([1,3,7,1,7,5], [1,9,2,5,1])
    q.run()

if __name__ == '__main__':
    main()
