from leeyzer import Solution, solution


class Q154(Solution):
    @solution
    def findMin(self, nums):
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:  # 排除有序的情况，因为切分后是两个有序数组
            return nums[lo]
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[lo]:  # 左侧有序，排除有序
                lo = mid
            elif nums[mid] < nums[lo]:  # 右侧有序，排除有序
                hi = mid
            elif nums[lo] <= nums[lo+1]:
                lo += 1
            else:
                return nums[lo+1]
        return nums[hi]

    @solution
    def findMin2(self, nums):
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # 这里需要边界检查
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]: # 逆序对在最前会被上面语句截断
                return nums[mid]
            if nums[mid] > nums[lo]:
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            # 全等数组lo会累加，所以也需要边界检查
            elif lo < len(nums)-1 and nums[lo] > nums[lo+1]:
                return nums[lo+1]
            else:
                lo += 1
        return nums[0]


def main():
    q = Q154()
    q.add_args([1, 3, 5])
    q.add_args([3, 3, 3])
    q.add_args([10, 1, 2, 3, 4, 5, 6, 7])
    q.add_args([10, 1, 10, 10, 10])
    q.run()


if __name__ == "__main__":
    main()
