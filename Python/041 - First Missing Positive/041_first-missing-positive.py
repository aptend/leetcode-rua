from leeyzer import Solution, solution


class Q041(Solution):
    @solution
    def firstMissingPositive(self, nums):
        # 16ms 94.92%
        N = len(nums)
        i = 0
        while i < N:
            # nums[i] == nums[nums[i]-1] covers two things:
            # 1. we find a duplicate number
            # 2. we have place current number in the right place
            if 1 <= nums[i] <= N and nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        i = 0
        while i < N and nums[i] == i+1:
            i += 1
        return i + 1



def main():
    q = Q041()
    q.add_args([1, 1])
    q.add_args([1, 2, 0])
    q.add_args([3, 1, 2])
    q.add_args([3, 4, -1, 1])
    q.add_args([7, 8, 9, 11, 12])
    q.run()


if __name__ == "__main__":
    main()
