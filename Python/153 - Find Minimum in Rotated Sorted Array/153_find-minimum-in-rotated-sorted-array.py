from leezy import Solution, solution


class Q153(Solution):
    @solution
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        if nums[lo] < nums[hi]:
            return nums[lo]
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[lo]:  # no equal here, loop break before mid = lo
                lo = mid
            else:
                hi = mid
        return nums[hi]

    @solution
    def find_min(self, nums):
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # no duplicates in array, save us from checking boundry
            # the inversed pair maybe the first two elements
            # so we check mid with its right neighbor
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] >= nums[lo]:
                lo = mid + 1 # mid is not the answer
            else:
                hi = mid - 1
        # no duplicates, so we will find answer in the loop


def main():
    q = Q153()
    q.add_case(q.case([3, 4, 5, 1, 2]).assert_equal(1))
    q.add_case(q.case([1, 2, 3, 4, 5]).assert_equal(1))
    q.add_case(q.case([5, 1, 2, 3, 4]).assert_equal(1))
    q.run()


if __name__ == "__main__":
    main()
