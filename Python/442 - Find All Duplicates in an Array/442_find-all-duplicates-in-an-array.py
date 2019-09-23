from leeyzer import Solution, solution


class Q442(Solution):
    @solution
    def findDuplicates(self, nums):
        # 452ms 21.95%
        # like 041 and 448
        N = len(nums)
        for i in range(N):
            while nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        ans = []
        for i in range(N):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans
    
    @solution
    def find_dup(self, nums):
        # 440ms
        # tricky
        ans = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                ans.append(abs(x))
            else:
                # make that position negative
                nums[abs(x)-1] *= -1
        return ans


def main():
    q = Q442()
    q.add_args([4, 3, 2, 7, 8, 2, 3, 1])
    q.run()


if __name__ == "__main__":
    main()
