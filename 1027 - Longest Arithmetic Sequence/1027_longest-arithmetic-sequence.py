from leeyzer import Solution, solution

from collections import defaultdict

class Q1027(Solution):
    @solution
    def longestArithSeqLength(self, A):
        # 2228ms 14.62%
        ans = 0
        dp = {}
        for i, a in enumerate(A):
            dp[i] = defaultdict(int)
            for j in range(i):
                delta = a - A[j]
                # pull from previous result
                # max is needed here because delta can be duplicated
                dp[i][delta] = max(dp[i][delta], dp[j][delta] + 1)
                ans = max(ans, dp[i][delta])
        return ans + 1
    
    @solution
    def longest_arith_seq_length(self, A):
        # 1380ms 64.80%
        dp = {}
        N = len(A)
        for i in range(N):
            for j in range(i+1, N):
                # push current result to following positions
                delta = A[j] - A[i]
                # current don't have previous delta, initiate dp[j, delta] with 2
                dp[j, delta] = dp.get((i, delta), 1) + 1
        # if there is not the warrant that N >= 2
        # we should handle special case to return 0 or 1
        dp[-1, -1] = 1 if N else 0
        return max(dp.values())




def main():
    q = Q1027()
    q.add_args([1]) # 1
    q.add_args([3, 3, 3, 3]) # 4
    q.add_args([3, 6, 9, 12]) # 4
    q.add_args([9, 4, 7, 2, 10]) # 3
    q.add_args([20, 1, 15, 3, 10, 5, 8]) # 4
    q.run()


if __name__ == "__main__":
    main()
