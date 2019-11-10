from leezy import Solution, solution


class Q713(Solution):
    @solution
    def numSubarrayProductLessThanK(self, nums, k):
        # 1008ms 81.63%
        if k <= 1:
            return 0
        N = len(nums)
        i, p, ans = 0, 1, 0
        for j in range(N):
            p *= nums[j]
            while p >= k:
                p //= nums[i]
                i += 1
            ans += j - i + 1
        return ans



def main():
    q = Q713()
    q.add_args([10, 5, 2, 6], 100)
    q.add_args([1, 2, 3, 4], 2)
    q.add_args([1, 2, 3, 4], 3)
    q.run()


if __name__ == "__main__":
    main()
