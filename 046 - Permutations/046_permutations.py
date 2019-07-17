from leeyzer import Solution, solution


class Q046(Solution):
    @solution
    def permute(self, nums):
        used = [False] * len(nums)
        current, total = [], []
        self.dfs(nums, 0, current, total, used)
        return total
    
    def dfs(self, nums, depth, current, total, used):
        if depth == len(nums):
            total.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            current.append(nums[i])
            used[i] = True
            self.dfs(nums, depth+1, current, total, used)
            used[i] = False
            current.pop()


def main():
    q = Q046()
    q.add_args([1, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
