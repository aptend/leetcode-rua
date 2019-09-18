from leeyzer import Solution, solution

from collections import defaultdict

class Q1010(Solution):
    @solution
    def numPairsDivisibleBy60(self, time):
        # 264ms 61.26%
        table = defaultdict(int)
        ans = 0
        for d in time:
                r = d % 60
                ans += table[(60 - r) % 60]
                table[r] += 1
        return ans


def main():
    q = Q1010()
    q.add_args([30, 20, 150, 100, 40])
    q.add_args([60, 60, 60])
    q.run()


if __name__ == "__main__":
    main()
