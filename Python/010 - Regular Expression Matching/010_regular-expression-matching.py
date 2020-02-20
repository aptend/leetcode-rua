from leezy import Solution, solution


class Q010(Solution):
    @solution
    def isMatch(self, s, p):
        # 16ms 99.82%
        m, n = len(s), len(p)
        memo = [[None] * (n+1) for _ in range(m+1)]

        def match(i, j):
            # when pattern is depleted, we see if str is also depleted
            if j == n:
                return i == m
            if memo[i][j] is not None:
                return memo[i][j]
            # when s is depleted while p is not, first_match is False
            first_match = i < len(s) and (p[j] == '.' or s[i] == p[j])
            if j < n - 1 and p[j+1] == '*':
                # anyway, we can try to skip the "*" pattern by j+2
                ans = match(i, j+2)
                # if first letter is matched, skip the letter from s, and
                # we have opportunity to keep the '*' pattern for next round,
                # or use it once here and drop it
                if first_match:
                    ans = ans or match(i+1, j) or match(i+1, j+2)
            else:
                # match letter, skip it
                ans = first_match and match(i+1, j+1)

            memo[i][j] = ans
            return ans
        return match(0, 0)


def main():
    q = Q010()
    q.add_case(q.case('', '.').assert_equal(False))
    q.add_case(q.case('aa', 'a').assert_equal(False))
    q.add_case(q.case("mississippi", "mis*is*p*.").assert_equal(False))
    q.add_case(q.case('aa', 'a*').assert_equal(True))
    q.add_case(q.case('ab', '.*').assert_equal(True))
    q.add_case(q.case('aab', 'c*a*b').assert_equal(True))
    q.run()


if __name__ == "__main__":
    main()
