from leezy import solution, Solution

from collections import Counter


class Q1002(Solution):
    @solution
    def commonChars(self, A):
        # 52ms 80.08%
        cs = [Counter(a) for a in A]
        ans = []
        for x in 'abcdefghijklmnopqrstuvwxyz':
            n = min(c[x] for c in cs)
            for _ in range(n):
                ans.append(x)
        return ans


def main():
    q = Q1002()
    q.add_case(q.case(['bella', 'label', 'roller']))
    q.run()


if __name__ == '__main__':
    main()
