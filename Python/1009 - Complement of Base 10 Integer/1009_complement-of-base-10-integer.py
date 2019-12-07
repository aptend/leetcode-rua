from leezy import solution, Solution


class Q1009(Solution):
    @solution
    def bitwiseComplement(self, N):
        # 28ms 87.13%
        if N == 0:
            return 1
        bits = []
        while N > 0:
            N, r = divmod(N, 2)
            bits.append(r)
        ans = 0
        for b in bits[::-1]:
            ans = ans * 2 + 1-b
        return ans


def main():
    q = Q1009()
    q.add_case(q.case(5).assert_equal(2))
    q.add_case(q.case(7).assert_equal(4))
    q.add_case(q.case(10).assert_equal(5))
    q.run()

if __name__ == '__main__':
    main()
