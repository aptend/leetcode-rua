from leeyzer import Solution, solution, timeit


class Q698(Solution):
    @timeit
    # @solution
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        target, r = divmod(total, k)
        if r != 0 or max(nums) > target:
            return False
        # nums = sorted(nums, reverse=True)
        return self.dfs(nums, 0, target, 0, k, 0)

    def dfs(self, nums, start, target, formed, k, used):
        """
        :nums: source numbers  
        :start: form current group using nums[start:]  
        :target: target group sum  
        :formed: current group sum  
        :k: we need `k` more groups  
        :used: bitmap recording whether nums[x] used  
        """
        if k == 0:
            return True
        for i in range(start, len(nums)):
            if (1 << i) & used or formed + nums[i] > target:
                continue
            new_formed = formed + nums[i]
            if new_formed == target and self.dfs(nums, 0, target, 0, k-1, (1 << i) | used):
                return True
            elif self.dfs(nums, start+1, target, new_formed, k, (1 << i) | used):
                return True
        return False
    
    @timeit
    @solution
    def can(self, nums, k):
        visit = [0 for i in range(len(nums))]
        target = sum(nums) // k

        def DFS(k, fromindex, cursum):
            if k == 1 and cursum == target:
                return True
            if cursum == target:
                return DFS(k-1, 0, 0)
            else:
                for i in range(fromindex, len(nums)):
                    if nums[i] + cursum <= target and not visit[i]:
                        visit[i] = 1
                        if DFS(k, i + 1, cursum + nums[i]):
                            return True
                        visit[i] = 0
                return False
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        return DFS(k, 0, 0)



def main():
    q = Q698()
    # q.add_args([4, 3, 2, 3, 5, 2, 1], 4)
    # q.add_args([1, 2, 1, 2, 2, 1, 2, 1], 4)
    # q.add_args([1, 2, 1, 2, 2, 1, 2, 1], 5)
    # q.add_args([10, 12, 1, 2, 10, 7, 5, 19, 13, 1], 4)
    # q.add_args([5, 4, 5, 3, 5, 5, 2, 1, 5, 3, 5, 5, 2, 5, 5, 5, 5, 5], 15)
    q.add_args([18, 20, 39, 73, 96, 99, 101, 111, 114, 190, 207, 295, 471, 649, 700, 1037], 4)
    q.run()


if __name__ == "__main__":
    main()
