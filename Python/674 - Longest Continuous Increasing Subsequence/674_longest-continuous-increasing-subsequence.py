from leezy import Solution, solution


class Q674(Solution):
    @solution
    def findLengthOfLCIS(self, nums):
        # 80ms 97.69%
        if not nums:
            return 0
        max_l, l = 1, 1
        for m, n in zip(nums, nums[1:]):
            if m < n:
                l += 1
            else:
                max_l = max(max_l, l)
                l = 0
        return max(max_l, l)


def main():
    q = Q674()
    q.add_args([1, 3, 5, 4, 7])
    q.run()


if __name__ == "__main__":
    main()
