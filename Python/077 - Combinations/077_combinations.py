from leeyzer import Solution, solution, timeit


class Q077(Solution):

    @timeit
    @solution
    def combine(self, n, k):
        if n == k:
            return [list(range(1, n+1))]
        if k == 1:
            return [[x] for x in range(1, n+1)]
        current, total = [], []
        nums = list(range(1, n+1))
        self.dfs(nums, k, 0, 0, current, total)
        return total

    def dfs(self, nums, k, depth, start, current, total):
        if depth == k:
            total.append(current[:])
            return
        # say, nums=[1,2,3,4,5,6], k=4
        # for 1st position, there's no need to try 4,5,6
        # for 2nd position, there's no need to try 5,6
        for i in range(start, len(nums) - (k-depth) + 1):
            current.append(nums[i])
            self.dfs(nums, k, depth+1, i+1, current, total)
            current.pop()


def main():
    q = Q077()
    q.add_args(4, 2)
    q.add_args(4, 4)
    q.add_args(4, 1)
    q.add_args(20, 10)
    q.run()


if __name__ == "__main__":
    main()
