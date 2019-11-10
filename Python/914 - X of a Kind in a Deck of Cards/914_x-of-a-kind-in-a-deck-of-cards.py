from leezy import Solution, solution
from collections import Counter


class Q914(Solution):
    @solution
    def hasGroupsSizeX(self, deck):
        # 152ms 93.04%
        counter = Counter(deck)
        def gcd(x, y):
            x, y = max(x, y), min(x, y)
            while y:
                x, y = y, x % y
            return x
        min_possible = next(iter(counter.values()))
        for v in counter.values():
            min_possible = gcd(min_possible, v)
            if min_possible == 1:
                return False
        return True

def main():
    q = Q914()
    q.add_args([1, 2, 3, 4, 4, 3, 2, 1])
    q.add_args([1, 1, 1, 2, 2, 2, 3, 3])
    q.add_args([1])
    q.add_args([1, 1])
    q.add_args([1, 1, 2, 2, 2, 2])
    q.run()


if __name__ == "__main__":
    main()
