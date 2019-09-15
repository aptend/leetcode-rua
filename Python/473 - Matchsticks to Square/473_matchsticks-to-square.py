from leeyzer import Solution, solution


class Q473(Solution):
    @solution
    def makesquare(self, nums):
        # 432ms 73.34%
        # same as 698 partition to k equal sum subsets
        N = len(nums)
        if N < 4:
            return False
        target, r = divmod(sum(nums), 4)
        nums = sorted(nums, reverse=True)
        if r != 0 or max(nums) > target:
            return False
        used = [False] * N

        def dfs(start, formed, k):
            if k == 0:
                return True
            for i in range(start, N):
                if used[i] or formed > target:
                    continue
                used[i] = True
                if formed + nums[i] == target:
                    found = dfs(0, 0, k-1)
                else:
                    found = dfs(i+1, formed+nums[i], k)
                if found:
                    return True
                used[i] = False
            return False
        return dfs(0, 0, 4)


def main():
    q = Q473()
    q.add_args([1, 1, 2, 2, 2])
    q.add_args([3, 3, 3, 3, 4])
    q.run()


if __name__ == "__main__":
    main()
