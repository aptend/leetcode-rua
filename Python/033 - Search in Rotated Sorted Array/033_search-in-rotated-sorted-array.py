"""
点在于通过二分找到有序的那一半，然后判断target在不在有序数组中来进一步收缩

if nums[mid] >= nums[lo]: # 等于如果发生，mid=lo => hi=(lo+1) or lo
                          
"""
from leezy import Solution, solution


class Q033(Solution):
    @solution
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]:  
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


def main():
    q = Q033()
    q.add_args([4, 5, 6, 7, 0, 1, 2], 0)
    q.add_args([4, 5, 6, 7, 0, 1, 2], 3)
    q.add_args([4, 5, 6, 7, 0, 1, 2], 4)
    q.add_args([4, 5, 6, 7, 0, 1, 2], 2)
    q.run()


if __name__ == "__main__":
    main()
