from leezy import Solution, solution


class Q664(Solution):
    @solution
    def strangePrinter(self, s):
        # 692ms 51.02%
        N = len(s)
        memo = {}

        def turns(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            min_ = turns(i, j-1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    min_ = min(min_, turns(i, k) + turns(k+1, j-1))
            memo[(i, j)] = min_
            return min_
        return turns(0, N-1)

    @solution
    def strange_printer_review(self, s):
        N = len(s)
        memo = {}

        def turns(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            min_ = turns(i+1, j) + 1  # print the first letter only
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    # the s[k] letter will be printed at the same time with
                    # the first letter
                    # so the two splitted interval doesn't include s[k] and
                    # the left interval includes s[i]
                    min_ = min(min_, turns(i, k-1) + turns(k+1, j))
            memo[(i, j)] = min_
            return min_
        return turns(0, N-1)

    @solution
    def printer_no_duplicates(self, s):
        # 356ms 99.05%
        s = ''.join([a for a, b in zip(s, '#'+s) if a != b])
        N = len(s)
        memo = [[0]*N for _ in range(N)]

        def count(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if memo[i][j] > 0:
                return memo[i][j]
            pivot = s[i]
            optimal = 1 + count(i+1, j)
            for k in range(i+1, j+1):
                if s[k] == pivot:
                    optimal = min(optimal, count(i+1, k)+count(k+1, j))
            memo[i][j] = optimal
            return optimal
        return count(0, N-1)


def main():
    q = Q664()
    q.add_case(q.case('').assert_equal(0))
    q.add_case(q.case('a').assert_equal(1))
    q.add_case(q.case('aaa').assert_equal(1))
    q.add_case(q.case('aaabbb').assert_equal(2))
    q.add_case(q.case('aba').assert_equal(2))
    q.add_case(q.case('caba').assert_equal(3))
    q.add_case(q.case('tbgtgb').assert_equal(4))  # b -> g -> t -> t => 4
    q.add_case(q.case('abcabcabc').assert_equal(7))
    q.add_case(q.case('abbbaa').assert_equal(2))
    q.run()


if __name__ == "__main__":
    main()
