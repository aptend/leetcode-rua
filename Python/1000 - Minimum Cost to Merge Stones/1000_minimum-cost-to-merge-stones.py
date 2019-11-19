from leezy import solution, Solution


class Q1000(Solution):
    @solution
    def mergeStones(self, stones, K):
        # 68ms 50.35%
        INF = float('inf')
        N = len(stones)
        prefix = [0] * (N + 1)
        # sum(stones[i..=j]) = prefix[j+1] - prefix[i]
        for i, x in enumerate(stones):
            prefix[i+1] = prefix[i] + x
        # the minimum cost of merging stones[i..=j] into m piles
        memo = {}

        def merge(i, j, m):
            if (j - i + 1 - m) % (K - 1) != 0:
                return INF
            if i == j and m == 1:
                return 0
            key = (i, j, m)
            if key in memo:
                return memo[key]
            if m == 1:
                cost = merge(i, j, K) + prefix[j+1] - prefix[i]
                memo[key] = cost
                return cost
            min_cost = min(merge(i, mid, 1) + merge(mid+1, j, m-1)
                           for mid in range(i, j, K-1))
            memo[key] = min_cost
            return min_cost

        ans = merge(0, N-1, 1)
        return -1 if ans == INF else ans


def main():
    q = Q1000()
    q.add_case(q.case([3, 2, 4, 1], 2).assert_equal(20))
    q.add_case(q.case([3, 2, 4, 1], 3).assert_equal(-1))
    q.add_case(q.case([3, 5, 1, 2, 6], 3).assert_equal(25))
    q.run()


if __name__ == '__main__':
    main()
