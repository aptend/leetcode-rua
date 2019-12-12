from leezy import solution, Solution


class Q1017(Solution):
    @solution
    def baseNeg2(self, N):
        # 20ms 99.51%
        if N == 0:
            return '0'
        ans = []
        l = 0
        while N > 0:
            if l % 2 == 0:
                N, r = divmod(N, 2)
            else:
                N, r = (N+1) // 2, N % 2
            ans.append(str(r))
            l += 1
        return ''.join(ans[::-1])


def main():
    q = Q1017()
    q.add_case(q.case(2).assert_equal("110"))
    q.add_case(q.case(3).assert_equal("111"))
    q.add_case(q.case(4).assert_equal("100"))
    q.run()


if __name__ == '__main__':
    main()
