from leezy import solution, Solution


class Q1358(Solution):
    @solution
    def numberOfSubstrings(self, s):
        # 240 ms 62.91%
        if len(s) < 3:
            return 0
        ca = cb = cc = 0
        i, j = 0, 0
        ans = 0
        N = len(s)
        while j < N:
            while j < N and (ca == 0 or cb == 0 or cc == 0):
                if s[j] == 'a':
                    ca += 1
                elif s[j] == 'b':
                    cb += 1
                else:
                    cc += 1
                j += 1
            while i < N and ca > 0 and cb > 0 and cc > 0:
                ans += N - j + 1
                if s[i] == 'a':
                    ca -= 1
                elif s[i] == 'b':
                    cb -= 1
                else:
                    cc -= 1
                i += 1
        return ans



def main():
    q = Q1358()
    q.add_case(q.case('abcabc').assert_equal(10))
    q.add_case(q.case('aaacb').assert_equal(3))
    q.add_case(q.case('acb').assert_equal(1))
    q.add_case(q.case('abab').assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
