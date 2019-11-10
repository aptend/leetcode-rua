from leezy import Solution, solution


class Q198(Solution):
    @solution
    def rob(self, nums):
        # dp0 means maximum money when previous house was not robbed
        # dp1 means maximum money when previous house was robbed
        dp0 = dp1 = 0
        for n in nums:
            new_dp0 = max(dp0, dp1) # skip this house
            dp1 = dp0 + n           # rob this house
            dp0 = new_dp0
        return max(dp0, dp1)

    @solution
    def rob2(self, nums):
        # dp0 means max money after CONSIDERING previous 2nd house, 
        # dp1 means max money after CONSIDERING previous 1st house
        dp0 = dp1 = 0
        for n in nums:
            new_dp1 = max(dp0 + n, dp1) # let's consider this house, rob or not
            dp0 = dp1
            dp1 = new_dp1
        return dp1


def main():
    q = Q198()
    q.add_args([1, 2, 3, 1]) # 4
    q.add_args([2, 7, 9, 3, 1]) # 12
    q.run()


if __name__ == "__main__":
    main()
