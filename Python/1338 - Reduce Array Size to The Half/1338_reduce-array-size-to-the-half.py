from leezy import solution, Solution
from collections import Counter


class Q1338(Solution):
    @solution
    def minSetSize(self, arr):
        # 640ms 65.25%
        c = Counter(arr)
        N = (len(arr) + 1) // 2
        ans = 0
        acc = 0
        for _, cnt in c.most_common():
            acc += cnt
            ans += 1
            if acc >= N:
                return ans


def main():
    q = Q1338()
    q.add_case(q.case([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]).assert_equal(2))
    q.add_case(q.case([3, 3, 3, 3, 3]).assert_equal(1))
    q.add_case(q.case([1, 9]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
