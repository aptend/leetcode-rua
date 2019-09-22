from leeyzer import Solution, solution


class Q1202(Solution):
    @solution
    def smallestStringWithSwaps(self, s, pairs):
        # 824ms
        N = len(s)
        adj = [[] for _ in range(N)]
        for v, w in pairs:
            adj[v].append(w)
            adj[w].append(v)

        state = [0] * N
        def dfs(v, cc):
            if state[v] == 1:
                return
            cc.append(v)
            state[v] = 1
            for w in adj[v]:
                dfs(w, cc)

        groups = []
        for i in range(N):
            if state[i] == 0:
                cc = []
                dfs(i, cc)
                groups.append(cc)
        ans = [''] * N
        for g in groups:
            for i, ch in zip(sorted(g), sorted(s[idx] for idx in g)):
                ans[i] = ch
        return ''.join(ans)



def main():
    q = Q1202()
    q.add_args('dcab', [[0, 3], [1, 2]])
    q.run()


if __name__ == "__main__":
    main()
