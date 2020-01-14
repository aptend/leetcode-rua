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


def main():
    q = Q1320()
    q.add_case(q.case('CAKE').assert_equal(3))
    q.add_case(q.case('HAPPY').assert_equal(6))
    q.add_case(q.case('NEW').assert_equal(3))
    q.add_case(q.case('YEAR').assert_equal(7))
    q.run()

if __name__ == '__main__':
    main()
