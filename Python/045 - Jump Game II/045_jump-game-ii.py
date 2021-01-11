from leezy import solution, Solution


class Q045(Solution):
    @solution
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        step = 0
        farest = 0
        next_farest = 0
        end = len(nums) - 1
        for i, d in enumerate(nums):
            if i + d > next_farest:
                next_farest = i + d
                if next_farest >= end:
                    return step + 1
            if i == farest:
                farest = next_farest
                step += 1

    @solution
    def jump1(self, nums):
        N = len(nums)
        dp = [float('inf')] * N
        dp[0] = 0
        for i in range(N-1):
            for dist in range(1, min(nums[i], N-1-i) + 1):
                dp[i+dist] = min(dp[i+dist], dp[i] + 1)
        return dp[-1]

def main():
    q = Q045()
    q.add_case(q.case([2, 3, 1, 1, 4]))
    q.run()


if __name__ == '__main__':
    main()
