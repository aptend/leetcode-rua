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

    @solution
    def find_min(self, nums):
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:  # 排除有序的情况，因为不存在旋转数组，实际上python的-1索引可用
            return nums[lo]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # 实际上，只要确保当前的比较顺序，并不需要边界检查
            # 合理的输入不可能mid=len(nums)，因为如果逆序对在最后两个，那么前一次循环已经找到了
            # mid=0可能，所以用现在这样的比较顺序，逆序对在头两个时可以先返回
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            # 没找到，自然应该排除mid，因为mid不是逆序对中的任何一个
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1


def main():
    q = Q153()
    q.add_args([3, 4, 5, 1, 2])
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([5, 1, 2, 3, 4])
    q.run()


if __name__ == "__main__":
    main()
