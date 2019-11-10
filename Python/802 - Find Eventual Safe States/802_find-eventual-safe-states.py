from leezy import Solution, solution
from enum import Enum


class Q802(Solution):
    @solution
    def eventualSafeNodes(self, graph):
        # 612ms 68.75%
        UNKOWN = 0  # 0 means this vertex has not been visited yet
        ON_STACK = 1  # 1 means this vertex is on stack, we are visiting
        SAFE = 2  # 2 means this vertex has been visited, and it is unsafe
        UNSAFE = 3  # 3 means this vertex has been visited, and it is safe
        V = len(graph)
        states = [UNKOWN] * V 
        def dfs(v):
            if states[v] == ON_STACK:
                states[v] = UNSAFE
                return UNSAFE
            if states[v] != UNKOWN:
                return states[v]
            states[v] = ON_STACK
            for w in graph[v]:
                if dfs(w) == UNSAFE: # dfs return either SAFE or UNSAFE
                    states[v] = UNSAFE
                    return UNSAFE
            # all outgoing edges will not enter a cycle
            states[v] = SAFE
            return SAFE
        ans = []
        for v in range(V):
            if dfs(v) == SAFE:
                ans.append(v)
        return ans



def main():
    q = Q802()
    q.add_args([[1, 2], [2, 3], [5], [0], [5], [], []])
    q.run()


if __name__ == "__main__":
    main()
