from leezy import Solution, solution


class Q1048(Solution):
    @solution
    def longestStrChain(self, words):
        # 1724ms 14.60%
        # variant of 300 longest increasing subsequence
        def is_follower(s, t):
            if len(t) - len(s) != 1:
                return False
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                else:
                    return s[i:] == t[i+1:]
            return True

        N = len(words)
        words = [''] + words
        words.sort(key=lambda x: len(x))
        dp = [0] * (N+1)
        for i in range(1, N+1):
            dp[i] = 0
            for j in range(i):
                if is_follower(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)

    @solution
    def longest_string_chain(self, words):
        # 116ms
        dp = {}
        for w in sorted(words, key=lambda x: len(x)):
            dp[w] = max(dp.get(w[:i]+w[i+1:], 0)+1 for i in range(len(w)))
        return max(dp.values())

def main():
    q = Q1048()
    q.add_args(['a', 'b', 'ba', 'bca', 'bda', 'bdca'])
    q.add_args(["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh",
        "gr", "grukmj", "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"])
    q.run()


if __name__ == "__main__":
    main()
