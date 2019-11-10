from leezy import Solution, solution


class Q926(Solution):
    @solution
    def minFlipsMonoIncr(self, S):
        def count1(s):
            return sum((c=='1' for c in s), 0)
        g_min = 2000
        for i in range(len(S)+1):
            alters = count1(S[0:i]) + len(S)-i-count1(S[i:])
            if alters < g_min:
                g_min = alters
        return g_min
    
    @solution
    def minFlip(self, S):
        acc = [0] * (len(S)+1) 
        # acc[i] how many 1 in S[:i+1]
        # acc[len(S)-1] total number of 1
        # acc[len(S)] is a 0 pad
        for i, c in enumerate(S):
            acc[i] = acc[i-1] + ord(c) - ord('0')
        N, g_min = len(S), 20000
        for i in range(N+1): # 1 starts from index i (0~N，i=N means S contains only 0)
            alters = acc[i-1] + N - i - (acc[N-1] - acc[i-1])
            if alters < g_min:
                g_min = alters
        return g_min
    
    @solution
    def minFlipDP(self, S):
        # dp[i][0] min flips to make ans[:i+1] be monotone and ans[i] = 0
        # dp[i][1] min flips to make ans[:i+1] be monotone and ans[i] = 1
        N = len(S)
        dp = [[0, 0] for _ in range(N+1)]
        for i, c in enumerate(S):
            if c == '0':
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        return min(dp[N-1][0], dp[N-1][1])

    @solution
    def DP_concise(self, S):
        dp0, dp1 = 0, 0
        for c in S:
            if c == '0':
                dp1 = min(dp0, dp1) + 1
            else:
                dp1 = min(dp0, dp1)
                dp0 += 1
        return min(dp0, dp1)



def main():
    q = Q926()
    q.add_args('00110')
    q.add_args('010110')
    q.add_args('00011000')
    q.run()


if __name__ == "__main__":
    main()
