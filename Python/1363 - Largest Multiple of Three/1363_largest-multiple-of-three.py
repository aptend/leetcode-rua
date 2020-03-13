from leezy import solution, Solution


class Q1363(Solution):
    @solution
    def largestMultipleOfThree(self, digits):
        # 264ms 5.6%
        # normal dp
        N = len(digits)
        MIN = float('-inf')
        dp = [[(0, 0)] * 3 for _ in range(N+1)]
        path = [[(-1, -1)] * 3 for _ in range(N+1)]
        dp[0] = [(0, 0), (MIN, 0), (MIN, 0)]
        for i in range(1, N+1):
            r = digits[i-1] % 3
            for j in range(3):
                k = (3 + j - r) % 3
                l, s = dp[i-1][k]
                candid = (l + 1, s + digits[i-1])
                if dp[i-1][j] >= candid:
                    dp[i][j] = dp[i-1][j]
                    path[i][j] = (i-1, j)
                else:
                    dp[i][j] = candid
                    path[i][j] = (i-1, k)
        chosen = []
        i, j = N, 0
        while True:
            ni, nj = path[i][j]
            if ni == -1 or nj == -1:
                break
            if dp[ni][nj] < dp[i][j]:
                chosen.append(digits[i-1])
            i, j = ni, nj
        ans = ''.join(str(d) for d in sorted(chosen, reverse=True))
        return '0' if ans.startswith('0') else ans

    @solution
    def largest(self, digits):
        # 108ms 48.71%
        ds = [[], [], []]
        for d in digits:
            ds[d%3].append(d)
        for arr in ds:
            arr.sort()
        r = sum(digits) % 3
        if r == 0:
            chosen = digits
        elif r == 1:
            # remove first element of ds[1]
            if len(ds[1]) == 0:
                chosen = ds[0]
            else:
                chosen = ds[0] + ds[1][1:] + ds[2]
        else:
            if len(ds[2]) == 0:
                chosen = ds[0]
            else:
                chosen = ds[0] + ds[1] + ds[2][1:]
        chosen.sort(reverse=True)
        if not chosen:
            return ''
        elif chosen[0] == 0:
            return '0'
        else:
            return ''.join(str(d) for d in chosen)

def main():
    q = Q1363()
    q.add_case(q.case([8, 5]).assert_equal(''))
    q.add_case(q.case([8, 1, 9]).assert_equal('981'))
    q.add_case(q.case([0, 0, 0]).assert_equal('0'))
    q.add_case(q.case([8, 7, 6, 1, 0]).assert_equal('8760'))
    q.add_case(q.case([1, 1, 3, 6, 1]).assert_equal('63111'))
    q.add_case(q.case([7, 1, 2, 4, 0, 0, 4, 0, 3, 8]).assert_equal('874431000'))
    q.run()


if __name__ == '__main__':
    main()
