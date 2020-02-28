from leezy import solution, Solution
from collections import deque


class Q1353(Solution):
    @solution
    def maxEvents(self, events):
        # 820ms 91.41%
        used_days = [False] * 100001
        ans = 0
        for s, e in sorted(events, key=lambda x: x[1]):
            for i in range(s, e+1):
                if not used_days[i]:
                    ans += 1
                    used_days[i] = True
                    break
        return ans

    @solution
    def max_events(self, events):
        # TLE 39/44
        # consider the input [[200, 300], [1, 10000]]
        # you can see the difference of the two solutions
        events = deque(sorted(events, key=lambda x: x[1]))
        min_d, max_d = min(e[0] for e in events), events[-1][1]
        ans = 0
        used_events = deque(False for _ in range(len(events)))
        for d in range(min_d, max_d+1):
            while events and events[0][1] < d:
                events.popleft()
                used_events.popleft()
            for i, e in enumerate(events):
                if not used_events[i] and e[0] <= d <= e[1]:
                    used_events[i] = True
                    ans += 1
                    break
        return ans


def main():
    q = Q1353()
    q.add_case(q.case([[1, 2], [2, 3], [3, 4]]).assert_equal(3))
    q.add_case(q.case([[1, 100000]]).assert_equal(1))
    q.add_case(q.case([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]])
                .assert_equal(7))
    q.add_case(q.case([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
