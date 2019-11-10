from leezy import Solution, solution


class Q078(Solution):
    @solution
    def subsets(self, nums):
        current, total = [], []
        self.dfs(nums, 0, current, total)
        return total
    
    def dfs(self, nums, start, current, total):
        total.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.dfs(nums, i+1, current, total)
            current.pop()


def main():
    q = Q078()
    q.add_args([1, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
