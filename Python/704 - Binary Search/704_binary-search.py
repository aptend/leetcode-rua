from leeyzer import Solution, solution


class Q704(Solution):
    @solution
    def search(self, nums, target):
        # 212ms 96.17%
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    @solution
    def search_(self, nums, target):
        # 212ms
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo == len(nums) or nums[lo] != target:
            return -1
        return lo

def main():
    q = Q704()
    q.add_args([-1, 0, 3, 5, 9, 12], 9)
    q.add_args([-1, 0, 3, 5, 9, 12], 2)
    q.run()


if __name__ == "__main__":
    main()
