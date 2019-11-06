from leeyzer import solution, Solution

class Q091(Solution):
    @solution
    def numDecodings(self, s):
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        for i, x in enumerate(s, 1):
            dp[i] += dp[i-1] if x != '0' else 0
            if i >= 2 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[N]



def main():
    q = Q091()
    q.add_args('12')
    q.add_args('226')
    q.add_args('012712')
    q.run()

if __name__ == '__main__':
    main()
