from leezy import Solution, solution


class Q039(Solution):
    @solution
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        total, curr = [], []
        self.dfs(candidates, target, 0, curr, total)
        return total

    def dfs(self, arr, target, s, curr, total):
        if target == 0:
            total.append(curr[:])
            return
        for i in range(s, len(arr)):
            if arr[i] > target:
                break
            curr.append(arr[i])
            self.dfs(arr, target - arr[i], i, curr, total)
            curr.pop()



def main():
    q = Q039()
    q.add_args([2, 2, 3, 6, 7], 7)
    q.run()


if __name__ == "__main__":
    main()
