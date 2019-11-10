from leezy import solution, Solution

class Q055(Solution):
    @solution
    def canJump(self, nums):
        # TLE 74/75
        N = len(nums)
        dp = [False] * N
        dp[N-1] = True
        for i in range(N-2, -1, -1):
            dp[i] = any(dp[j] for j in range(min(N-1, i+nums[i]), 0, -1))
        return dp[0]
    
    @solution
    def can_jump(self, nums):
        # 92ms 98.65%
        N = len(nums)
        can_jump_index = N - 1
        for i in range(N-2, -1, -1):
            if i + nums[i] >= can_jump_index:
                can_jump_index = i
        return can_jump_index == 0



def main():
    q = Q055()
    q.add_args([2, 3, 1, 1, 4])
    q.add_args([3, 2, 1, 0, 4])
    q.run()

if __name__ == '__main__':
    main()
