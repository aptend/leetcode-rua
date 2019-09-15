from leeyzer import Solution, solution


class Q216(Solution):
    @solution
    def combinationSum3(self, k, n):
        curr, total = [], []
        self.dfs(n, k, 0, 1, curr, total)
        return total

    def dfs(self, target, depth, d, s, curr, total):
        if depth == d and target == 0:
            total.append(curr[:])
        for i in range(s, 10):
            if i > target:
                break
            curr.append(i)
            self.dfs(target-i, depth, d+1, i+1, curr, total)
            curr.pop()



def main():
    q = Q216()
    q.add_args(3, 7)
    q.add_args(3, 9)
    q.run()


if __name__ == "__main__":
    main()
