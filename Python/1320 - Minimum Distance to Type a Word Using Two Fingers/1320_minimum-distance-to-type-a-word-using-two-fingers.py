from leezy import solution, Solution


class Q1320(Solution):

    def cost(self, src, dst):
        if src == 26:
            return 0
        sx, sy = divmod(src, 6)
        dx, dy = divmod(dst, 6)
        return abs(sx-dx) + abs(sy-dy)

    @solution
    def min_distance(self, word):
        # 520 ms, faster than 36.18%
        memo = {}

        # solve(i, chx, chy): what is the min cost to type word[i..] when
        # the left finger is on chx and the right finger is on chy
        def solve(i, chx, chy):
            if i == len(word):
                return 0
            if (i, chx, chy) in memo:
                return memo[i, chx, chy]
            ch = ord(word[i]) - ord('A')
            ans = min(solve(i+1, ch, chy) + self.cost(chx, ch),
                      solve(i+1, chx, ch) + self.cost(chy, ch))
            memo[i, chx, chy] = ans
            return ans
        return solve(0, 26, 26)

    @solution
    def min_distance_better(self, word):
        # 256 ms, faster than 91.13%
        N = len(word)
        memo = [[None] * 27 for _ in range(N)]

        # solve(i, chx): what is the min cost to type word[i..] when
        # one finger is on word[i-1] and another is on chx(chx != word[i-1])
        def solve(i, chx):
            if i == len(word):
                return 0
            if memo[i][chx] is not None:
                return memo[i][chx]
            chy = ord(word[i-1]) - ord('A') if i > 0 else 26
            ch = ord(word[i]) - ord('A')
            ans = min(solve(i+1, chx) + self.cost(chy, ch),
                      solve(i+1, chy) + self.cost(chx, ch))
            memo[i][chx] = ans
            return ans
        return solve(0, 26)

    @solution
    def min_distance_dp_push(self, word):
        # 228ms, 92.34%
        N = len(word)
        MAX = float('inf')
        dp = [[MAX] * 27 for _ in range(N)]
        dp[0][26] = 0
        for i in range(N-1):
            cur_ch = ord(word[i]) - ord('A')
            nxt_ch = ord(word[i+1]) - ord('A')
            for j in range(27):
                if not dp[i][j] < MAX:  # we just push possible values
                    continue
                dp[i+1][j] = min(dp[i+1][j],
                                 dp[i][j] + self.cost(cur_ch, nxt_ch))
                dp[i+1][cur_ch] = min(dp[i+1][cur_ch],
                                      dp[i][j] + self.cost(j, nxt_ch))
        return min(dp[N-1])


def main():
    q = Q1320()
    q.add_case(q.case('CAKE').assert_equal(3))
    q.add_case(q.case('HAPPY').assert_equal(6))
    q.add_case(q.case('NEW').assert_equal(3))
    q.add_case(q.case('YEAR').assert_equal(7))
    q.run()


if __name__ == '__main__':
    main()
