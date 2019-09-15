from leeyzer import Solution, solution


class Q035(Solution):
    @solution
    def searchInsert(self, nums, target):
        # 28ms 97.42%
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

def main():
    q = Q035()
    q.add_args([1, 3, 5, 6], 5)
    q.add_args([1, 3, 5, 6], 2)
    q.add_args([1, 3, 5, 6], 7)
    q.run()


if __name__ == "__main__":
    main()
