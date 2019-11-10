from leezy import Solution, solution


class Q646(Solution):
    @solution
    def findLongestChain(self, pairs):
        # 248ms 62.80%
        lower = float('-inf')
        pairs.sort(key=lambda p: p[1])
        cnt = 0
        for p in pairs:
            if p[0] > lower:
                cnt += 1
                lower = p[1]
        return cnt

    @solution
    def find_longest_chain(self, pairs):
        # 2372ms
        N = len(pairs)
        pairs.sort()
        dp = [0] * N
        for i in range(N):
            max_len = 0
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
        return max(dp)




def main():
    q = Q646()
    q.add_args([[1, 2], [2, 3], [3, 4]])
    q.run()


if __name__ == "__main__":
    main()
