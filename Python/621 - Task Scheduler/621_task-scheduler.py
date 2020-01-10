from leezy import solution, Solution


class Q621(Solution):
    @solution
    def leastInterval(self, tasks, n):
        # 484ms 55.16%
        counter = [0] * 26
        for ch in tasks:
            counter[ord(ch) - ord('A')] += 1
        ans = 0

        def ensure_order():
            counter.sort(reverse=True)
            while counter and counter[-1] == 0:
                counter.pop()

        ensure_order()
        while True:
            max_assgin = min(n+1, len(counter))
            for i in range(max_assgin):
                counter[i] -= 1
            ensure_order()
            if not counter:
                ans += max_assgin
                break
            else:
                ans += n + 1

        return ans

    @solution
    def interval(self, tasks, n):
        # the basic idea is to fill n+1 slots with totally different tasks
        counter = [0 for _ in range(26)]
        for t in tasks:
            counter[ord(t) - ord('A')] += 1
        counter.sort()
        time = 0
        while counter[-1] > 0:
            for i in range(n+1):
                if counter[-1] <= 0:
                    break
                if i < 26 and counter[25-i] > 0:
                    counter[25-i] -= 1
                time += 1
            counter.sort()
        return time


def main():
    q = Q621()
    q.add_case(q.case(['A', 'A', 'A', 'B', 'B', 'B'], 2).assert_equal(8))
    q.add_case(q.case(['A', 'A', 'A', 'B', 'B', 'B'], 50).assert_equal(104))
    q.add_case(q.case(['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2).assert_equal(16))
    q.run()


if __name__ == '__main__':
    main()
