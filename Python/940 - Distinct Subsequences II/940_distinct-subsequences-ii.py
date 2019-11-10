from leezy import solution, Solution

from collections import Counter

class Q940(Solution):
    @solution
    def distinctSubseqII(self, S):
        # TLE 93/109
        N = len(S)
        # dp[i] means how many subseq ending with S[i]
        # initialize dp with 1, because, 
        # for 'abcc', 
        # dp[0] has at least 'a'
        # 'ab' for dp[1], 'abc' for dp[2], 'abcc' for dp[3]
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if S[i] != S[j]:
                    dp[i] += dp[j]
        return sum(dp) % (10**9 + 7)
    
    @solution
    def distinct_subseq(self, S):
        # 112ms 19.91%
        # dp[0] means how many subseqs ending with 'a'
        # dp[25] means how many subseqs ending with 'z'
        dp = [0] * 26
        for ch in S:
            dp[ord(ch) - ord('a')] = sum(dp) + 1
        return sum(dp) % (10**9 + 7)

    @solution
    def distinct_subseq_ii(self, S):
        # 64ms
        ans = 0
        dp = Counter()
        for ch in S:
            old_ans = ans
            ans += ans + 1 - dp[ch]
            dp[ch] = old_ans + 1
        return ans % (10**9 + 7)



def main():
    q = Q940()
    q.add_args('abc')
    q.add_args('aba')
    q.add_args('aaa')
    q.run()

if __name__ == '__main__':
    main()
