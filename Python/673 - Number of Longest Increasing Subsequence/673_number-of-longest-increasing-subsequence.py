from leezy import Solution, solution

class Q673(Solution):
    @solution
    def findNumberOfLIS(self, nums):
        # Python3 1476ms 5.19%
        if not nums:
            return 0
        N = len(nums)
        # dp[i] means max length of LIS ending with nums[i]
        dp = [0 for _ in range(N)]
        # dp_n[i] means numbers of LIS ending with nums[i]
        dp_n = [0 for _ in range(N)]
        for i in range(N):
            dp[i] = 1 + max((dp[j] for j in range(i) if nums[j] < nums[i]),
                            default=0)
            n = sum(dp_n[j] for j in range(i) if dp[j] == dp[i]-1 and nums[j] < nums[i])
            # n = 0 means nums[i] can't be attached to any seqs,
            # LIS is itself alone, only one
            dp_n[i] = n if n > 0 else 1
        max_len = max(dp)
        return sum(dp_n[j] for j in range(N) if dp[j] == max_len)

    @solution
    def numberOfLIS(self, nums):
        # 712ms 77.65%
        if not nums:
            return 0
        N = len(nums)
        dp = [1 for _ in range(N)]
        dp_n = [0 for _ in range(N)]
        for i in range(N):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] >= max_len:
                        max_len = dp[j] + 1
                        count = 0
                    if dp[j] == max_len - 1:
                        count += dp_n[j]
            dp[i] = max_len
            dp_n[i] = count if count > 0 else 1
        max_len = max(dp)
        return sum(dp_n[j] for j in range(N) if dp[j] == max_len)



def main():
    q = Q673()
    q.add_args([1, 3, 5, 4, 7]) # 2
    q.add_args([1, 2, 4, 3, 5, 4, 7, 2]) # 3
    q.add_args([2, 2, 3, 2]) # 2
    q.run()


if __name__ == "__main__":
    main()
