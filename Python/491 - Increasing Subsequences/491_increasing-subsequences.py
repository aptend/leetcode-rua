from leezy import Solution, solution


class Q491(Solution):
    @solution
    def findSubsequences(self, nums):
        # 252ms 75.14%
        N = len(nums)
        def dfs(s, cur, total):
            if len(cur) >= 3:
                total.append(cur[1:])
            used = set()
            for i in range(s, N):
                x = nums[i]
                if x >= cur[-1] and x not in used:
                    used.add(x)
                    cur.append(x)
                    dfs(i+1, cur, total)
                    cur.pop()
        cur, total = [float('-inf')], []
        dfs(0, cur, total)
        return total


def main():
    q = Q491()
    q.add_args([4, 6, 7, 7])
    q.add_args([1, 2, 1, 1, 1])
    q.run()

   

if __name__ == "__main__":
    main()
