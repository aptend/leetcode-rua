"""
点在于，原来可以通过判断mid和lo的大小来判断有序数组，等于时的情况不能说明问题了
原来nums[mid]和nums[lo]相等，可以明确地说，mid = lo, 左边有序依旧得到保证
但是考虑[4,5,0,4,4,4,4]，相等无法说明左边有序
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
            # mid不是解，所以把开头的mid全部删除
            while lo < mid and nums[lo] == nums[mid]:
                lo += 1
            # 如果因为不等跳出循环，下面一个会取大于
            # 如果因为lo = mid跳出循环，下面一定会取等于
            if nums[mid] >= nums[lo]:  # 左侧一定就是有序数组
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:                      # 右侧一定是有序数组
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False

    @solution
    def search2(self, nums, target):
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
            else:         # nums[mid] < nums[lo]
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return False


def main():
    q = Q081()
    q.add_args([2, 5, 6, 0, 0, 1, 2], 0)
    q.add_args([2, 5, 6, 0, 0, 1, 2], 3)
    q.add_args([2, 5, 6, 0, 0, 1, 2], -1)
    q.run()


if __name__ == "__main__":
    main()
