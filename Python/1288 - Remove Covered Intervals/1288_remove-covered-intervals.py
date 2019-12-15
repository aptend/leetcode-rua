from leezy import solution, Solution


class Q1288(Solution):
    @solution
    def removeCoveredIntervals(self, intervals):
        # 100ms
        V = sorted(intervals, key=lambda v: (v[0], v[0] - v[1]))
        limit = V[0][1]
        ans = 1
        for v in V[1:]:
                if v[1] > limit:
                    limit = v[1]
                    ans += 1
        return ans


def main():
    q = Q1288()
    q.add_case(q.case([[1, 4], [3, 6], [2, 8]]))
    q.run()

if __name__ == '__main__':
    main()
