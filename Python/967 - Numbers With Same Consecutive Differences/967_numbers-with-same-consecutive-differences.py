from leeyzer import Solution, solution


class Q967(Solution):
    @solution
    def numsSameConsecDiff(self, N, K):
        # 72ms 8.05%
        if N == 1:
            return list(range(10))

        def dfs(n, cur, total):
            if n == 0:
                ans = 0
                for i in range(N):
                    ans = 10 * ans + cur[i]
                total.append(ans)
                return
            for i in range(10):
                if i == 0 and len(cur) == 0:
                    continue
                if len(cur) == 0 or abs(i - cur[-1]) == K:
                    cur.append(i)
                    dfs(n-1, cur, total)
                    cur.pop()
        cur = []
        total = []
        dfs(N, cur, total)
        return total

    @solution
    def nums_same_consec_diff(self, N, K):
        # 40ms 98.66%
        # apply same idea in problem [1215 stepping numbers] in biweek contest 10
        if N == 1:
            return list(range(10))
        dp = list(range(1, 10))
        for _ in range(N-1):
            new_dp = []
            for x in dp:
                r = x % 10
                if r >= K:
                    new_dp.append(x*10 + r - K)
                if K and r <= 9 - K:
                    new_dp.append(x*10 + r + K)
            dp = new_dp
        return dp



def main():
    q = Q967()
    q.add_args(3, 7)
    q.add_args(2, 1)
    q.add_args(2, 0)
    q.add_args(1, 1)
    q.run()


if __name__ == "__main__":
    main()
