from leeyzer import Solution, solution


class Q1052(Solution):
    @solution
    def maxSatisfied(self, customers, grumpy, X):
        # 256ms 86.15%
        base_sum = 0
        N = len(customers)
        for i in range(N):
            if grumpy[i] == 0:
                base_sum += customers[i]
                customers[i] = 0
        # find max sliding window sum with size X
        max_win_sum = win_sum = sum(customers[:X])
        for i, j in zip(range(N), range(X, N)):
            win_sum += (customers[j] - customers[i])
            max_win_sum = max(win_sum, max_win_sum)
        return base_sum + max_win_sum


def main():
    q = Q1052()
    q.add_args([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
    q.run()


if __name__ == "__main__":
    main()
