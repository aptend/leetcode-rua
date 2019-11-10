from leezy import Solution, solution


class Q886(Solution):
    @solution
    def possibleBipartition(self, N, dislikes):
        # same with 785 is graph bipartite?
        graph = [[] for _ in range(N)]
        for pair in dislikes:
            graph[pair[0]-1].append(pair[1]-1)
            graph[pair[1]-1].append(pair[0]-1)
        
        states = [0] * N

        def dfs(x, color):
            states[x] = color
            for nxt in graph[x]:
                if states[nxt] == color:
                    return False
                if states[nxt] != 0:
                    continue
                if not dfs(nxt, -color):
                    return False
            return True

        for i in range(N):
            if states[i] != 0:
                continue
            if not dfs(i, 1):
                return False
        return True


def main():
    q = Q886()
    q.add_args(4, [[1, 2], [1, 3], [2, 4]])
    q.add_args(3, [[1, 2], [1, 3], [2, 3]])
    q.add_args(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
    q.run()


if __name__ == "__main__":
    main()
