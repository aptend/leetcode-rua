from leezy import Solution, solution


class Q033(Solution):
    @solution
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            # the left part is sorted
            if nums[mid] >= nums[lo]:
                # so we ask if the target is in the sorted array
                # and then narrow search range, according to the result
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # the right part is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


def main():
    q = Q033()
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 0).assert_equal(4))
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 3).assert_equal(-1))
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 4).assert_equal(0))
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 2).assert_equal(6))
    q.run()


if __name__ == "__main__":
    main()
