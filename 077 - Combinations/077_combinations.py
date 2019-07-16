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
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.dfs(nums, k, depth+1, i+1, current, total)
            current.pop()

    @timeit
    @solution
    def combine_from_lc(self, n, k):
        def _combine(start, k_left, chosen, combinations):
            if k_left == 0:
                combinations.append(chosen[:])
            else:
                # We should iterate until the point when there are
                # not enough values until `n` to fill `k_left` slots that we need.
                # "+2" to account for range() stop condition, and other off-by-one.
                i_when_not_enough_left = n - k_left + 2

                for i in range(start, i_when_not_enough_left, 1):
                    chosen.append(i)
                    # Since `i` was chosen, make next call choose from i+1 onwards.
                    _combine(i + 1, k_left - 1, chosen, combinations)
                    chosen.pop()

        combinations = []
        _combine(1, k, [], combinations)
        return combinations



def main():
    q = Q077()
    q.add_args(4, 2)
    q.add_args(4, 4)
    q.add_args(4, 1)
    q.add_args(20, 10)
    q.run()


if __name__ == "__main__":
    main()
