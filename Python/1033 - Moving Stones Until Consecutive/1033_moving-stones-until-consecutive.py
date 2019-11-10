from leezy import solution, Solution

class Q1033(Solution):
    @solution
    def numMovesStones(self, a, b, c):
        # 20ms 100.00%
        a, b, c = sorted([a, b, c])
        max_s = c - a - 2
        if a + 1 == b and b + 1 == c:
            return [0, max_s]
        if a + 1 == b or b + 1 == c:
            return [1, max_s]
        if b - a == 2 or c - b == 2:
            return [1, max_s]
        return [2, max_s]


def main():
    q = Q1033()
    q.add_args(1, 2, 5)
    q.run()

if __name__ == '__main__':
    main()
