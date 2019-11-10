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
            min_ = turns(i+1, j) + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    min_ = min(min_, turns(i+1, k-1) + turns(k, j))
            memo[(i, j)] = min_
            return min_
        return turns(0, N-1)
    
    @solution
    def printer_no_duplicates(self, s):
        # 372ms 96.64#
        s = ''.join([a for a, b in zip(s, '#'+s) if a != b])
        N = len(s)
        memo = {}

        def turns(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            min_ = turns(i+1, j) + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    min_ = min(min_, turns(i+1, k-1) + turns(k, j))
            memo[(i, j)] = min_
            return min_
        return turns(0, N-1)


def main():
    q = Q664()
    q.add_args('')
    q.add_args('a')
    q.add_args('aaa')
    q.add_args('aaabbb')
    q.add_args('aba')
    q.add_args('caba')
    q.add_args('tbgtgb') # b -> g -> t -> t => 4
    q.run()


if __name__ == "__main__":
    main()
