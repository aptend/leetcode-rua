from leezy import solution, Solution


class Q1042(Solution):
    @solution
    def gardenNoAdj(self, N, paths):
        # 432ms  99.58%
        adj = [[] for _ in range(N+1)]
        for v, w in paths:
            adj[v].append(w)
            adj[w].append(v)
        ans = [0] * (N + 1)
        for v in range(1, N+1):
            colors = [False] * 4
            for w in adj[v]:
                if ans[w] > 0:
                    colors[ans[w]-1] = True
            for i, c in enumerate(colors, 1):
                if not c:
                    ans[v] = i
                    break
        return ans[1:]


def main():
    q = Q1042()
    q.add_case(q.case(3, [[1, 2], [2, 3], [3, 1]]))
    q.add_case(q.case(4, [[1, 2], [3, 4]]))
    q.add_case(q.case(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
    q.add_case(q.case(5, [[3, 4], [4, 5], [3, 2], [5, 1], [1, 3], [4, 2]]))
    q.run()


if __name__ == '__main__':
    main()
