from leeyzer import Solution, solution


class Q034(Solution):
    @solution
    def searchRange(self, nums, target):
        # 60ms 98.92% / 72ms
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        start = lo
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [start, lo-1]


def main():
    q = Q034()
    q.add_args([5, 7, 7, 8, 8, 10], 8)
    q.add_args([5, 7, 7, 8, 8, 10], 6)
    q.run()


if __name__ == "__main__":
    main()
