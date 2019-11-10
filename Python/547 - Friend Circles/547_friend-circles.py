from leezy import Solution, solution


class Q547(Solution):
    @solution
    def findCircleNum(self, M):
        # basic verison (using `seen`) is in 200. numbers of islands
        N = len(M)
        def dfs(i):
            M[i][i] = 0
            for j in range(N):
                if M[i][j] == 1:
                    M[i][j] = M[j][i] = 0
                    dfs(j)
        cc_count = 0
        for i in range(N):
            if M[i][i] == 1:
                dfs(i)
                cc_count += 1
        return cc_count



def main():
    q = Q547()
    q.add_args([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    q.add_args([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    q.run()


if __name__ == "__main__":
    main()
