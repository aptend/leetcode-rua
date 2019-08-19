from leeyzer import Solution, solution
from collections import deque


class Q785(Solution):
    @solution
    def isBipartite(self, graph):
        # 144ms 99.78% / 156ms
        N = len(graph)
        seen = [False] * N
        setA = set()
        setA.add(0)
        setB = set()
        q = deque()
        for i in range(N):
            if seen[i]:
                continue
            q.append(i)
            while q:
                for _ in range(len(q)):
                    v = q.popleft()
                    for nxt in graph[v]:
                        if nxt in setA:
                            return False
                        if seen[nxt]:
                            continue
                        seen[nxt] = True
                        setB.add(nxt)
                        q.append(nxt)
                setA, setB = setB, setA
        return True
    
    @solution
    def is_bipartite_bfs_color(self, graph):
        # graph coloring bfs 152ms
        # 1 means red and -1 means blue
        N = len(graph)
        states = [0] * N
        q = deque()
        for i in range(N):
            if states[i] != 0:
                continue
            q.append(i)
            states[i] = 1 # a new connected component. assign either color
            while q:
                for _ in range(len(q)):
                    v = q.popleft()
                    for nxt in graph[v]:
                        if states[nxt] == states[v]:
                            return False
                        if states[nxt] != 0:
                            continue
                        states[nxt] = -states[v]
                        q.append(nxt)
        return True
    
    @solution
    def is_bipartite_dfs_color(self, graph):
        # dfs 148ms
        N = len(graph)
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
    q = Q785()
    q.add_args([[1, 3], [0, 2], [1, 3], [0, 2]])
    q.add_args([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    q.add_args([[], [3], [], [1], []]) # True
    q.add_args([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], 
                [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
                [2, 4, 5, 6, 7, 8]])  # False
    q.run()


if __name__ == "__main__":
    main()
