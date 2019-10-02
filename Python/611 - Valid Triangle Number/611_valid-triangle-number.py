from leeyzer import Solution, solution

from bisect import bisect_left

class Q611(Solution):
    @solution
    def triangleNumber(self, nums):
        # 592ms 36.03%
        N = len(nums)
        if N < 3:
            return 0
        nums = sorted(nums)
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                idx = bisect_left(nums, nums[i]+nums[j], j+1, N)
                ans += idx - 1 - j
        return ans
    
    @solution
    def tiangle_number(self, nums):
        # 256ms 80.14%
        A = sorted(nums)
        N = len(A)
        ans = 0
        # lock k and scan smaller i and j
        for k in range(2, N):
            i = 0
            j = k - 1
            while i < j:
                if A[i] + A[j] > A[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans




def main():
    q = Q611()
    q.add_args([2, 2, 3, 4])
    q.add_args([2, 2, 3, 4, 45, 4, 12, 7])
    q.run()


if __name__ == "__main__":
    main()
