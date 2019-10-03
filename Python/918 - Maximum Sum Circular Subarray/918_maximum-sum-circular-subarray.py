from leeyzer import Solution, solution


class Q918(Solution):
    @solution
    def maxSubarraySumCircular(self, A):
        dp0 = 0
        dp1 = 0
        max_ = float('-inf')
        min_ = float('inf')
        for x in A:
            dp0 = max(x, dp0+x)
            max_ = max(max_, dp0)
            dp1 = min(x, dp1+x)
            min_ = min(min_, dp1)
        sum_ = sum(A)
        if sum_ == min_:
            return max_
        else:
            return max(max_, sum_ - min_)



def main():
    q = Q918()
    q.add_args([1, -2, 3, -2])
    q.add_args([5, -3, 5])
    q.add_args([3, -1, 2, -1])
    q.add_args([3, -2, 2, -3])
    q.add_args([-2, -3, -1])
    q.add_args([-2, 4, -5, 4, -5, 9, 4])
    q.run()


if __name__ == "__main__":
    main()
