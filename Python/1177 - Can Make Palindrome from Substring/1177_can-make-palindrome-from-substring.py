from leezy import Solution, solution
from collections import Counter

class Q1177(Solution):
    @solution
    def canMakePaliQueries(self, s, queries):
        # Brute solution. TLE
        ans = [True] * len(queries)
        for i, (l, r, k) in enumerate(queries):
            if k < 13:
                d = Counter(s[l: r + 1])
                odds = len([0 for ct in d.values() if ct % 2])
                ans[i] = odds // 2 <= k
        return ans

    @solution
    def pali_queries(self, s, queries):
        # 1684ms 41.12%
        state = 0
        states = [0] * (len(s) + 1)
        BASE = ord('a')
        for i, ch in enumerate(s, 1):
            state ^= 1 << (ord(ch) - BASE)
            states[i] = state
        ans = []
        for i, j, k in queries:
            if k >= 13:
                ans.append(True)
                continue
            sole = states[i] ^ states[j+1]
            cnt_ones = 0
            while sole:
                cnt_ones += 1
                sole &= sole - 1
            ans.append(cnt_ones // 2 <= k)
        return ans


def main():
    q = Q1177()
    q.add_args('abcda', [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]])
    q.run()


if __name__ == "__main__":
    main()
