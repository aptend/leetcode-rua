from leezy import solution, Solution


class Q1006(Solution):
    @solution
    def clumsy(self, N):
        # 32ms 95.82%
        solo = [1, 2, 6]
        if N < 4:
            return solo[N-1]
        ans = N * (N-1) // (N-2) + (N-3)
        for n in range(N-4, 3, -4):
            ans -= n * (n-1) // (n-2) - (n-3)
        if N % 4 > 0:
            ans -= solo[N%4-1]
        return ans


def main():
    q = Q1006()
    q.add_case(q.case(4).assert_equal(7))
    q.add_case(q.case(10).assert_equal(12))
    q.run()

if __name__ == '__main__':
    main()
