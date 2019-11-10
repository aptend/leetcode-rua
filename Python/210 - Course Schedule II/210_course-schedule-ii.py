from leezy import Solution, solution


class Q210(Solution):
    @solution
    def findOrder(self, numCourses, prerequisites):
        # 76ms 95.20%
        V = numCourses
        adj = [[] for _ in range(V)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        seen = [False] * V
        on_stack = [False] * V
        order = []
        def dfs(v):
            seen[v] = True
            on_stack[v] = True
            for w in adj[v]:
                if not seen[w]:
                    if dfs(w):
                        return True
                elif on_stack[w]:
                    return True
            order.append(v)
            on_stack[v] = False
            return False

        for v in range(V):
            if not seen[v]:
                if dfs(v):  # found a cycle
                    return []
        return order

    @solution
    def order(self, numCourses, prerequisites):
        # 80ms
        V = numCourses
        adj = [[] for _ in range(V)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        # 0 means this vertex has not been visited yet
        # 1 means this vertex is on stack, we are visiting
        # 2 means this vertex has been visited
        states = [0] * V
        order = []
        def dfs(v):
            if states[v] == 2:
                return False
            if states[v] == 1:
                return True
            states[v] = 1
            for w in adj[v]:
                if dfs(w):
                    return True
            order.append(v)
            states[v] = 2
            return False
        for v in range(V):
            if dfs(v):
                return []
        return order




def main():
    q = Q210()
    q.add_args(2, [[1, 0]])
    q.add_args(2, [[1, 0], [0, 1]])
    q.add_args(4, [[1, 0], [2, 0], [3, 2], [3, 1]])
    q.run()


if __name__ == "__main__":
    main()
