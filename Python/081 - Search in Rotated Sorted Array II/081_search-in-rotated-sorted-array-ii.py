"""
in problem 33, A[mid] >= A[lo], we can say the left array is sorted.

however, in this case, we can't do that again.

consider this array [4,5,0,4,4,4,4], we have 4(mid) >= 4(lo), but the left
array is unsorted.

how can we reduce this case to what we have been familiar with?

we can eliminate all leading elements who equal A[mid], then we are able to

determine which part is sorted, like what we did in problem 33.
"""

from leezy import Solution, solution


class Q081(Solution):
    @solution
    def search1(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            while lo < mid and nums[lo] == nums[mid]:
                lo += 1
            # now the left array is sorted, maybe nums[mid] **is** nums[lo]
            if nums[mid] >= nums[lo]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False

    @solution
    def search2(self, nums, target):
        # the mirror version
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            while nums[hi] == nums[mid] and hi > mid:
                hi -= 1
            if nums[mid] <= nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return False


def main():
    q = Q081()
    q.add_case(q.case([2, 5, 6, 0, 0, 1, 2], 0).assert_equal(True))
    q.add_case(q.case([2, 5, 6, 0, 0, 1, 2], 3).assert_equal(False))
    q.add_case(q.case([2, 5, 6, 0, 0, 1, 2], -1).assert_equal(False))
    q.run()


if __name__ == "__main__":
    main()
