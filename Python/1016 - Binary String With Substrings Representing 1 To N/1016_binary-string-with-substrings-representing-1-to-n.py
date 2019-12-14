from leezy import solution, Solution


class Q1016(Solution):
    @solution
    def queryString(self, S, N):
        # 24ms 98% tricky
        if N > 2000:
            return False
        return all(bin(n)[2:] in S for n in range(N, N // 2, -1))


def main():
    q = Q1016()
    q.add_case(q.case('0110', 3).assert_equal(True))
    q.add_case(q.case('0110', 4).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
