from leezy import Solution, solution


class Q740(Solution):
    @solution
    def deleteAndEarn(self, nums):
        # 108ms
        vals = [0] * 10001
        for n in nums:
            vals[n] += n
        dp1 = dp2 = 0
        for i in range(len(vals)):
            tmp = max(dp2+vals[i], dp1)
            dp2 = dp1
            dp1 = tmp
        return dp1
    
    @solution
    def delete_earn(self, nums):
        # 40ms
        if not nums:
            return 0
        min_, max_ = min(nums), max(nums)
        vals = [0] * (max_-min_+1)
        for n in nums:
            vals[n-min_] += n
        dp1 = dp2 = 0
        for i in range(len(vals)):
            tmp = max(dp2+vals[i], dp1)
            dp2 = dp1
            dp1 = tmp
        return dp1
    



def main():
    q = Q740()
    q.add_args([3, 4, 2])  # 6
    q.add_args([2, 2, 3, 3, 3, 4])  # 9
    q.run()


if __name__ == "__main__":
    main()
