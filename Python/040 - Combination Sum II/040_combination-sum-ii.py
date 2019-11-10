from leezy import Solution, solution


class Q040(Solution):
    @solution
    def combinationSum2(self, candidates, target):
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
            # when i > s, we have tried the first element at least
            # we don't want to try duplicates for **current depth(length)**
            # Given sorted array, arr[i] = arr[i-1] reminds us to skip
            # if arr[i] != arr[i-1], obviously, it is a new element 
            # for **current depth(position)**, give it a shoot
            if i > s and arr[i-1] == arr[i]:
                continue
            curr.append(arr[i])
            self.dfs(arr, target - arr[i], i+1, curr, total)
            curr.pop()


def main():
    q = Q040()
    q.add_args([10, 1, 2, 7, 6, 1, 5], 8)
    q.run()


if __name__ == "__main__":
    main()
