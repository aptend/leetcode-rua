from leezy import solution, Solution

from collections import defaultdict


class Q1245(Solution):
    @solution
    def treeDiameter(self, edges):
        # this is similiar with 543. binary tree diameter
        # the only difference is that we don't kown root here
        # so we need to maintain two longest value to figure out the longest path include current node

        graph = defaultdict(list)
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)

        self.ans = 0

        def dfs(v, prev):
            max1 = max2 = 0
            for w in graph[v]:
                if w == prev:
                    continue
                l = dfs(w, v)
                if l > max1:
                    max1, max2 = l, max1
                elif l > max2:
                    max2 = l
                self.ans = max(self.ans, max1+max2)
            return max1 + 1
        return dfs(0, -1)

    @solution
    def tree_dia(self, edges):

        graph = defaultdict(list)
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)

        # do dfs from node x,update maxlength and end point.
        self.farest_node = None
        self.max_len = 0
        def dfs(v, prev, length):
            if len(graph[v]) == 1 and graph[v][0] == prev: # end point
                if length > self.max_len:
                    self.max_len = length
                    self.farest_node = v
            for w in graph[v]:
                if w != prev:
                    dfs(w, v, length+1)

        dfs(0, None, 0)
        dfs(self.farest_node, None, 0)
        return self.max_len


def main():
    q = Q1245()
    q.add_case(q.case([[0, 1], [0, 2]])
                .assert_equal(2))
    q.add_case(q.case([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]])
                .assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
