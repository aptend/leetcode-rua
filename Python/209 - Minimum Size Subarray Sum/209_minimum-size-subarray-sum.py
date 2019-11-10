from leezy import Solution, solution


class Q209(Solution):
    @solution
    def minSubArrayLen(self, s, nums):
        # 56ms 82.79%
        N = len(nums)
        i, j = 0, 0
        ans = N+1
        subsum = 0
        while True:
            while j < N and subsum < s:
                subsum += nums[j]
                j += 1
            while i < N and subsum >= s:
                subsum -= nums[i]
                i += 1
            ans = min(ans, j-i+1)
            if j == N:
                break
        return ans if ans <= N else 0


def main():
    q = Q209()
    q.add_args(7, [])
    q.add_args(7, [2, 3, 1, 2, 4, 3])
    q.add_args(13, [2, 3, 1, 2, 4, 3])
    q.add_args(15, [2, 3, 1, 2, 4, 3])
    q.add_args(20, [2, 3, 1, 2, 4, 3])
    q.run()


if __name__ == "__main__":
    main()
