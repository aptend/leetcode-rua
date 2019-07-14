from leeyzer import Solution, solution


class Q198(Solution):
    @solution
    def rob(self, nums):
        dp1 = dp2 = 0
        for n in nums:
            tmp = max(n+dp2, dp1)
            dp2 = dp1
            dp1 = tmp
        return dp1

def main():
    q = Q198()
    q.add_args([1, 2, 3, 1]) # 4
    q.add_args([2, 7, 9, 3, 1]) # 12
    q.run()


if __name__ == "__main__":
    main()
