from leezy import solution, Solution


class Q997(Solution):
    @solution
    def findJudge(self, N, trust):
        # 764ms 99.09%
        cands = [True] * (N+1)
        votes = [0] * (N+1)
        for t in trust:
            cands[t[0]] = False
            votes[t[1]] += 1
        for i in range(1, N+1):
            if cands[i] and votes[i] == N-1:
                return i
        return -1


def main():
    q = Q997()
    q.add_case(q.case(2, [[1, 2]]).assert_equal(2))
    q.add_case(q.case(3, [[1, 3], [2, 3], [3, 1]]).assert_equal(-1))
    q.run()


if __name__ == '__main__':
    main()
