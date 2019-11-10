from leezy import Solution, solution

from bisect import bisect_right

class Q826(Solution):
    @solution
    def maxProfitAssignment(self, difficulty, profit, worker):
        # 348ms 51.20%
        N = len(difficulty)
        idx = sorted(range(N), key=lambda x: difficulty[x])
        max_profit = [0] * N
        sort_difficulty = [0] * N
        max_ = -1
        for i, pos in enumerate(idx):
            sort_difficulty[i] = difficulty[pos]
            max_ = max(max_, profit[pos])
            max_profit[i] = max_
        ans = 0
        for w in worker:
            i = bisect_right(sort_difficulty, w) - 1
            if i >= 0:
                ans += max_profit[i]
        return ans




def main():
    q = Q826()
    q.add_args([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    q.add_args([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [1, 2, 4, 5, 6, 7, 20])
    q.add_args([5, 50, 92, 21, 24, 70, 17, 63, 30, 53],
               [68, 100, 3, 99, 56, 43, 26, 93, 55, 25],
               [96, 3, 55, 30, 11, 58, 68, 36, 26, 1])
    q.run()


if __name__ == "__main__":
    main()
