from leeyzer import Solution, solution


class Q044(Solution):
    """
    和10.regular expression matching相似了
    """
    @solution
    def isMatch_beta(self, s, p):
        m, n = len(s), len(p)

        def match(i, j):
            if i == m and j == n:  # s, p都耗尽
                return True
            if j == n:  # p耗尽，但是s还有
                return False

            # p没有耗尽
            if i == m:  # s耗尽
                if p[j] == '*':
                    return match(i, j+1)
                else:
                    return False

            # s没有耗尽
            if p[j] == '?' or p[j] == s[i]:
                return match(i+1, j+1)
            elif p[j] == '*':
                # *匹配n个字符，等效于n次match(i+1, j)，最后一次match(i, j+1)
                return match(i, j+1) or match(i+1, j)
            else:
                return False
        return match(0, 0)

    @solution
    def isMatch_release(self, s, p):
        m, n = len(s), len(p)
        memo = [[None]*(n+1) for _ in range(m+1)]

        def match(i, j):
            # p耗尽
            if j == n:
                return i == m
            if memo[i][j] is not None:
                return memo[i][j]
            s_avail = i < m
            # 不论s是否耗尽，遇到*，都要执行match(i, j+1)，然后视情况match(i+1, j)
            if p[j] == '*':
                memo[i][j] = match(i, j+1) or s_avail and match(i+1, j)
            else:
                first_match = s_avail and p[j] in (s[i], '?')
                memo[i][j] = first_match and match(i+1, j+1)
            return memo[i][j]
        return match(0, 0)


def main():
    q = Q044()
    q.add_args('aa', 'a')
    q.add_args('aa', '*')
    q.add_args('aa', '**')
    q.add_args('aa', '**?')
    q.add_args('cb', '?a')
    q.add_args('adceb', '*a*b')
    q.run()


if __name__ == "__main__":
    main()
