from leezy import solution, Solution

from bisect import bisect_right


class Q031(Solution):
    @solution
    def nextPermutation(self, nums):
        # 40ms 92.02%
        N = len(nums)
        if len(nums) <= 1:
            return nums
        for i in range(N-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return nums
        pivot = i
        # reverse descreasing subarray
        i += 1
        j = N - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        idx = bisect_right(nums, nums[pivot], pivot+1, N)
        nums[pivot], nums[idx] = nums[idx], nums[pivot]
        return nums


def main():
    q = Q031()
    q.add_case(q.case([1, 2, 3]).assert_equal([1, 3, 2]))
    q.add_case(q.case([3, 2, 1]).assert_equal([1, 2, 3]))
    q.add_case(q.case([1, 1, 5]).assert_equal([1, 5, 1]))
    q.add_case(q.case([1, 5, 1]).assert_equal([5, 1, 1]))
    q.add_case(q.case([1, 4, 5, 5, 2, 1]).assert_equal([1, 5, 1, 2, 4, 5]))
    q.run()


if __name__ == '__main__':
    main()
