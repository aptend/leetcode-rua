from leezy import Solution, solution


class Q022(Solution):
    @solution
    def generateParenthesis(self, n):
        total = []
        self.dfs(0, n, '', total)
        return total

    def dfs(self, open, n, current, total):
        if open == 0 and n == 0:
            total.append(current)
            return
        if n > 0:
            self.dfs(open+1, n-1, current+'(', total)
        if open > 0:
            self.dfs(open-1, n, current+')', total)


def main():
    q = Q022()
    q.add_args(3)
    q.run()


if __name__ == "__main__":
    main()
