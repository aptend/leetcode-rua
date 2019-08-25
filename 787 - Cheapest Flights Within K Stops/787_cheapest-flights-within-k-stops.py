from leeyzer import Solution, solution
from collections import namedtuple
from heapq import heappush, heappop

class Q787(Solution):
    @solution
    def findCheapestPrice(self, n, flights, src, dst, K):
        # 80ms 63.63%
        edge = namedtuple('edge', 'from_ to weight')
        graph = [[] for _ in range(n)]
        for f in flights:
            graph[f[0]].append(edge(f[0], f[1], f[2]))
        heap = [(0, src, K+1)]
        while heap:
            cost, city, k = heappop(heap)
            if city == dst:
                return cost
            if k:
                for e in graph[city]:
                    # we save every possible cost for dist_to[v]
                    heappush(heap, (cost+e.weight, e.to, k-1))
        return -1

    @solution
    def cheapest_flight(self, n, flights, src, dst, K):
        # 140ms
        # dp[k][i] means min cost from src to i by at most k flights(k-1 stops)
        MAX = float('inf')
        dp = [[MAX]*n for _ in range(K+2)]
        dp[0][src] = 0
        for k in range(1, K+2): # Bellman-Ford algorithm with recording explicit dist_to version(k hops)
            dp[k][src] = 0
            for from_, to, cost in flights:
                # this is RELAXing edge (from_, to) !!
                dp[k][to] = min(dp[k][to], dp[k-1][from_]+cost)
        ans = dp[K+1][dst]
        return -1 if ans == MAX else ans




def main():
    q = Q787()
    q.add_args(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
    q.add_args(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
    q.add_args(4, [[0, 1, 100], [1, 2, 100], 
                   [2, 0, 500], [3, 1, 200]], 0, 3, 6)
    q.add_args(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
               0, 3, 1)
    q.run()


if __name__ == "__main__":
    main()
