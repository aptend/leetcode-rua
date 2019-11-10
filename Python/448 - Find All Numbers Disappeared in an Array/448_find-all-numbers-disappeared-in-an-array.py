from leezy import Solution, solution


class Q448(Solution):
    @solution
    def findDisappearedNumbers(self, nums):
        # 356ms 25.28%
        # link to 041.first missing positive
        N = len(nums)
        for i in range(N):
            while nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        ans = []
        for i in range(N):
            if nums[i] != i + 1:
                ans.append(i+1)
        return ans


def main():
    q = Q448()
    q.add_args([4, 3, 2, 7, 8, 2, 3, 1])
    q.run()


if __name__ == "__main__":
    main()
