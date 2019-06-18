from leeyzer import Solution, solution


class Q153(Solution):
    @solution
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        if nums[lo] < nums[hi]:  # 排除有序的情况，因为切分后是两个有序数组
            return nums[lo]
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[lo]:  # 无法取到等号，等号成立时，mid=lo，已经跳出循环了
                lo = mid
            else:                     # 小于
                hi = mid
        return nums[hi]


def main():
    q = Q153()
    q.add_args([3, 4, 5, 1, 2])
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([5, 1, 2, 3, 4])
    q.run()


if __name__ == "__main__":
    main()
