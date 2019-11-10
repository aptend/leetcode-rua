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
            s_avail = i < m
            # when s is depleted while p is not, head_match is False
            head_match = s_avail and (s[i] == p[j] or p[j] == '.')
            if j < n - 1 and p[j+1] == '*':
                # "*" pattern, which can handle empty s
                ans = match(i, j+2)
                if head_match:
                    # when head matchs, use '*' once or more
                    ans = ans or match(i+1, j) or match(i+1, j+2)
            else:
                # '.' pattern alone or no pattern, skip if we can
                ans = head_match and match(i+1, j+1)

            memo[i][j] = ans
            return ans
        return match(0, 0)


def main():
    q = Q010()
    q.add_args('', '.')
    q.add_args('aa', 'a')
    q.add_args('aa', 'a*')
    q.add_args('ab', '.*')
    q.add_args('aab', 'c*a*b')
    q.add_args(s="mississippi", p="mis*is*p*.")
    q.run()


if __name__ == "__main__":
    main()
