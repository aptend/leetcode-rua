from leeyzer import Solution, solution


class Q053(Solution):
    @solution
    def maxSubArray(self, nums):
        # 52ms 60%
        ans = nums[0]
        # dp means the maximum of a subarray ending with current num
        dp = ans
        for x in nums[1:]:
            dp = max(dp+x, x)
            ans = max(ans, dp)
        return ans

    @solution
    def max_divide_conquer(self, nums):
        # 112ms 5% O(nlogn)
        def max_sub_cross(lo, mid, hi):
            right_max, right_sum = 0, 0
            for x in nums[mid+1:hi+1]:
                right_sum += x
                right_max = max(right_max, right_sum)

            left_max, left_sum = 0, 0
            for x in reversed(nums[lo:mid]):
                left_sum += x
                left_max = max(left_max, left_sum)
            return right_max + nums[mid] + left_max

        def max_subarray(lo, hi):
            if lo > hi:
                return float('-inf')

            mid = lo + (hi - lo) // 2
            return max(
                max_subarray(lo, mid-1),
                max_subarray(mid+1, hi),
                max_sub_cross(lo, mid, hi)
            )
        
        return max_subarray(0, len(nums)-1)

            
def main():
    q = Q053()
    q.add_args([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    q.add_args([8, -19, 5, -4, 20])
    q.run()


if __name__ == "__main__":
    main()
