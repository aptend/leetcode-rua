from leeyzer import Solution, solution


class Q162(Solution):
    @solution
    def findPeakElement(self, nums):
        # 28ms 89.04%
        lo, hi = 0, len(nums)-1
        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] < nums[m+1]:
                lo = m + 1
            else:
                hi = m
        return lo

def main():
    q = Q162()
    q.add_args([1])
    q.add_args([2, 1])
    q.add_args([1, 2])
    q.add_args([1, 2, 3, 1])
    q.add_args([1, 2, 1, 3, 5, 6, 4])
    q.run()


if __name__ == "__main__":
    main()
