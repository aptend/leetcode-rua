from leeyzer import Solution, solution


class Q494(Solution):
    @solution
    def push_v1(self, nums, S):
        total = sum(nums)
        if total < abs(S):
            return 0
        offset, capacity = total, total * 2 + 1
        dp = [0] * capacity
        dp[offset] = 1
        for n in nums:
            cur_dp = [0] * capacity
            for i in range(0, capacity):
                if i - n >= 0:
                    cur_dp[i-n] += dp[i]
                if i + n < capacity:
                    cur_dp[i+n] += dp[i]
            dp = cur_dp
        return dp[S+offset]

    @solution
    def push_v2(self, nums, S):
        total = sum(nums)
        if total < abs(S):
            return 0
        offset, capacity = total, total * 2 + 1
        dp = [0] * capacity
        dp[offset] = 1
        for n in nums:
            cur_dp = [0] * capacity
            # dp两侧第一个非零数，一定是1，索引为前k个数的sum、-sum
            # 随着迭代，两边的1向外扩张，直到最后一个n，设为n'，
            # dp[n'], dp[capacity-n']为1，所以对任意n，都有
            # dp[0, n]、dp[capacity-n, capacity]为0，对push没有贡献
            for i in range(n, capacity-n):
                if dp[i]:
                    cur_dp[i-n] += dp[i]
                    cur_dp[i+n] += dp[i]
            dp = cur_dp
        return dp[S+offset]

    @solution
    def pull(self, nums, S):
        total = sum(nums)
        if total < abs(S):
            return 0
        offset, capacity = total, total * 2 + 1
        dp = [0] * capacity
        dp[offset] = 1
        for n in nums:
            cur_dp = [0] * capacity
            for i in range(0, capacity):
                if i - n >= 0:
                    cur_dp[i] += dp[i-n]
                if i + n < capacity:
                    cur_dp[i] += dp[i+n]
            dp = cur_dp
        return dp[S+offset]

    @solution
    def sack01_push(self, nums, S):
        total = sum(nums)
        if total < abs(S) or (abs(S)+total) % 2 == 1:
            return 0
        subset_s = (total + S) // 2
        dp = [0] * (subset_s + 1)
        dp[0] = 1
        for n in nums:
            cur_dp = dp[:]  # copy, 小于n的情况直接沿用上次dp的结果
            for i in range(subset_s+1-n):
                cur_dp[i+n] += dp[i]
            dp = cur_dp
        return dp[subset_s]

    @solution
    def sack01_pull(self, nums, S):
        total = sum(nums)
        if total < abs(S) or (abs(S)+total) % 2 == 1:
            return 0
        subset_s = (total + S) // 2
        dp = [0] * (subset_s + 1)
        dp[0] = 1
        for n in nums:
            cur_dp = dp[:]  # copy, 小于n的情况直接沿用上次dp的结果
            for i in range(n, subset_s+1):
                cur_dp[i] += dp[i-n]
            dp = cur_dp
        return dp[subset_s]

    @solution
    def sack01_pull_rev(self, nums, S):
        total = sum(nums)
        if total < abs(S) or (abs(S)+total) % 2 == 1:
            return 0
        subset_s = (total + S) // 2
        dp = [0] * (subset_s + 1)
        dp[0] = 1
        for n in nums:
            # in-place pull，小于n的情况同样是沿用
            for i in range(subset_s, n-1, -1):
                dp[i] += dp[i-n]
        return dp[subset_s]

    @solution
    def dfs(self, nums, S):
        def _dfs(nums, depth, target, output):
            if depth == len(nums):
                if target == 0:
                    output[0] += 1
                return
            n = nums[depth]
            _dfs(nums, depth+1, target+n, output)
            _dfs(nums, depth+1, target-n, output)
        total = sum(nums)
        if total < abs(S):
            return 0
        output = [0]
        _dfs(nums, 0, S, output)
        return output[0]



def main():
    q = Q494()
    q.add_args([1, 1, 1, 1, 1], 3)  # 5
    q.add_args([1, 2, 3, 3, 4], 3)  # 3
    q.add_args([1, 2, 3, 3, 4], 1)  # 4
    q.add_args([1, 1, 1, 1, 1], 4)  # 0
    q.add_args([1, 1, 1, 1, 1], 100)  # 0
    q.add_args([1, 1, 2, 1, 2], -3)  # 5
    q.run()


if __name__ == "__main__":
    main()
