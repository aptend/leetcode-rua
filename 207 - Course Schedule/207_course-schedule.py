from leeyzer import Solution, solution


class Q207(Solution):
    @solution
    def canFinish(self, numCourses, prerequisites):
        # 80ms 71.79%
        V = numCourses
        adj = [[] for _ in range(V)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        seen = [False] * V
        on_stack = [False] * V

        def dfs(v):
            seen[v] = True
            on_stack[v] = True
            for w in adj[v]:
                if not seen[w]:
                    if dfs(w):
                        return True
                elif on_stack[w]:
                    return True
            on_stack[v] = False
            return False

        for v in range(V):
            if not seen[v]:
                if dfs(v): # found a cycle
                    return False
        return True
    
    @solution
    def can_finish(self, numCourses, prerequisites):
        # 68ms 99.38%
        UNKOWN = 0
        ON_STACK = 1
        VISITED = 2
        V = numCourses
        adj = [[] for _ in range(V)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        states = [UNKOWN] * V
        def dfs(v):
            if states[v] == ON_STACK:
                return True
            elif states[v] == VISITED:
                return False
            states[v] = ON_STACK
            for w in adj[v]:
                if dfs(w):
                    return True
            states[v] = VISITED
            return False
        for v in range(V):
            if dfs(v):
                return False
        return True



def main():
    q = Q207()
    q.add_args(2, [[1, 0]])
    q.add_args(2, [[1, 0], [0, 1]])
    q.run()


if __name__ == "__main__":
    main()
