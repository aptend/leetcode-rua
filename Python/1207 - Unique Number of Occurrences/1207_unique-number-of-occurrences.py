from leezy import Solution, solution

from collections import Counter

class Q1207(Solution):
    @solution
    def uniqueOccurrences(self, arr):
        # 48ms
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(cnt)


def main():
    q = Q1207()
    q.add_args([1, 2, 2, 1, 1, 3])
    q.run()


if __name__ == "__main__":
    main()
