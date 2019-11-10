from leezy import Solution, solution


class Q139(Solution):
    @solution
    def wordBreak(self, s, wordDict):
        # review search method
        # 28ms 63.07% / TLE w/o memo
        word_dict = set(wordDict)
        memo = {}
        def dfs(i, formed):
            if i >= len(s):
                return formed == ''
            if i in memo:
                return memo[i]
            for j in range(i, len(s)):
                formed += s[j]
                if formed in word_dict and dfs(j+1, ''):
                    return True
            memo[i] = False
            return False
        return dfs(0, '')

    @solution
    def word_break_dp(self, s, wordDict):
        # 24ms 81.60% / 32ms
        N = len(s)
        word_dict = set(wordDict)
        dp = [False for _ in range(N+1)]
        dp[0] = True
        for i in range(1, N+1):
            for j in range(i-1, -1, -1):
                if s[j:i] in word_dict and dp[j]:
                    dp[i] = True
                    break
        return dp[N]

def main():
    q = Q139()
    q.add_args('leetcode', ['leet', 'code'])
    q.add_args('apppenapp', ['app', 'pen'])
    q.add_args('catsandog', ["cats", "dog", "sand", "and", "cat"])
    q.run()


if __name__ == "__main__":
    main()
