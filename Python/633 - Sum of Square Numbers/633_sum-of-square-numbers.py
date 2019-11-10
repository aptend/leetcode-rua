from leezy import Solution, solution
from math import sqrt

class Q633(Solution):
    @solution
    def judgeSquareSum(self, c):
        # 124ms 74.87%
        hay = [n*n for n in range(int(sqrt(c)+1))]
        i, j = 0, len(hay)-1
        while i <= j:
            s = hay[i] + hay[j]
            if s == c:
                return True
            elif s > c:
                j -= 1
            else:
                i += 1
        return False


def main():
    q = Q633()
    q.add_args(2)
    q.add_args(4)
    q.add_args(5)
    q.add_args(8)
    q.run()


if __name__ == "__main__":
    main()
