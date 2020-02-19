from leezy import Solution, solution


class Q154(Solution):
    @solution
    def findMin(self, nums):
        """this solution aims at finding the inversed pair

        when the loop ends, the two digits left are the inversed pair
        """
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:  # original array is sorted
            return nums[lo]
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[lo]:    # left array is sorted, exclude
                lo = mid                # keep mid, maybe it is the minimum
            elif nums[mid] < nums[lo]:  # right array is sorted, exclude
                hi = mid
            elif nums[lo] <= nums[lo+1]:  # move lo when nums[lo] == nums[mid]
                lo += 1
            else:
                # if nums[lo] > nums[lo+1], we find the answer
                return nums[lo+1]

        return nums[hi]

    @solution
    def find_min(self, A):
        lo, hi = 0, len(A) - 1
        if A[lo] < A[hi]:
            return A[lo]
        while hi - lo > 1:
            m = lo + (hi - lo) // 2
            if A[lo] == A[m]:  # handle this case explicitly
                while lo < m and A[lo] == A[m]:
                    lo += 1
                if A[lo] < A[m]:
                    return A[lo]
                elif A[lo] > A[m]:
                    return A[m]
            elif A[lo] < A[m]:
                lo = m
            else:
                hi = m
        return A[hi]

    @solution
    def findMin2(self, nums):
        """we can find the inversed pair in the loop
        """
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # firstly,
            # we check if the mid and its neighbors are the inversed pair
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:  # right neighbor
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:  # left neighbor
                return nums[mid]
            if nums[mid] > nums[lo]: # left array is sorted
                lo = mid + 1  # mid is not the answer, it is safe to exclude it
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            # what if all elements are equal? we have to check boundary
            elif lo < len(nums)-1 and nums[lo] > nums[lo+1]:
                return nums[lo+1]
            else:
                lo += 1
        return nums[0]


def main():
    q = Q154()
    q.add_case(q.case([1, 3, 5]).assert_equal(1))
    q.add_case(q.case([3, 5, 1]).assert_equal(1))
    q.add_case(q.case([3, 3, 3]).assert_equal(3))
    q.add_case(q.case([10, 1, 2, 3, 4, 5, 6, 7]).assert_equal(1))
    q.add_case(q.case([10, 1, 10, 10, 10]).assert_equal(1))
    q.run()


if __name__ == "__main__":
    main()
