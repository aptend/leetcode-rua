from leezy import Solution, solution


class Q090(Solution):
    @solution
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        current, total_set = [], set()
        self.dfs_set(nums, 0, current, total_set)
        total = []
        for soln in total_set:
            total.append(list(soln))
        return total

    def dfs_set(self, nums, start, current, total_set):
        total_set.add(tuple(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.dfs_set(nums, i+1, current, total_set)
            current.pop()

    @solution
    def subsets_with_dup(self, nums):
        nums = sorted(nums)
        current, total = [], []
        self.dfs_no_set(nums, 0, current, total)
        return total

    def dfs_no_set(self, nums, start, current, total):
        total.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.dfs_no_set(nums, i+1, current, total)
            current.pop()


def main():
    q = Q090()
    q.add_args([1, 2, 2])
    q.add_args([2, 1, 2, 2])
    q.run()


if __name__ == "__main__":
    main()
