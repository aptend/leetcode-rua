from leeyzer import Solution, solution


class Q047(Solution):
    @solution
    def permuteUnique(self, nums):
        used = [False] * len(nums)
        current, total = [], []
        nums = sorted(nums)
        self.dfs(nums, 0, current, total, used)
        return total

    def dfs(self, nums, depth, current, total, used):
        if depth == len(nums):
            total.append(current[:])
            return
        prev_used = None
        for i in range(len(nums)):
            if used[i] or nums[i] == prev_used:
                continue
            used[i] = True
            current.append(nums[i])
            prev_used = nums[i]
            self.dfs(nums, depth+1, current, total, used)
            current.pop()
            used[i] = False


def main():
    q = Q047()
    q.add_args([1, 1, 2])
    q.add_args([1, 1, 1])
    q.add_args([1, 1, 2, 2])
    q.run()


if __name__ == "__main__":
    main()
