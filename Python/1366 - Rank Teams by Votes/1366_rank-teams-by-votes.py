from leezy import solution, Solution


class Q1366(Solution):
    @solution
    def rankTeams(self, votes):
        # 84 ms faster than 38.10%
        N = len(votes[0])
        base = ord('A')
        stat = [[0] * N + [26-i] for i in range(26)]
        for vote in votes:
            for i, t in enumerate(vote):
                stat[ord(t)-base][i] += 1
        stat.sort(reverse=True)
        return ''.join(chr(26-s[-1]+base) for s in stat[:N])


def main():
    q = Q1366()
    q.add_case(q.case(['ABC', 'ACB', 'ABC', 'ACB', 'ACB'])
                .assert_equal('ACB'))
    q.add_case(q.case(["M", "M", "M", "M"])
                .assert_equal('M'))
    q.add_case(q.case(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
                .assert_equal('ZMNAGUEDSJYLBOPHRQICWFXTVK'))
    q.add_case(q.case(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"])
                .assert_equal('ABC'))
    q.add_case(q.case(["WXYZ", "XYZW"])
                .assert_equal('XWYZ'))
    q.run()


if __name__ == '__main__':
    main()
