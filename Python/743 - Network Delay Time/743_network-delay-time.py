from leezy import Solution, solution

from heapq import heappop, heappush
from collections import deque
class Q743(Solution):
    @solution
    def networkDelayTime(self, times, N, K):
        # 392ms 97.48%
        graph = [[] for _ in range(N)]
        for from_, to, delay in times:
            graph[from_-1].append((to-1, delay))
        MAX = float('inf')
        delay_to = [MAX] * N
        delay_to[K-1] = 0
        heap = [(0, K-1)]
        relaxed = set()
        while heap:
            _, v = heappop(heap)
            if v in relaxed:
                continue
            relaxed.add(v)
            for w, delay in graph[v]:
                if delay_to[w] > delay_to[v] + delay:
                    delay_to[w] = delay_to[v] + delay
                    heappush(heap, (delay_to[w], w))
        ans = max(delay_to)
        return -1 if ans == MAX else ans
    
    @solution
    def network_delay_time(self, times, N, K):
        # 536ms
        # Bellman-Ford using queue
        # No negative weighted cycle
        graph = [[] for _ in range(N)]
        for from_, to, delay in times:
            graph[from_-1].append((to-1, delay))
        MAX = float('inf')
        delay_to = [MAX] * N
        delay_to[K-1] = 0
        queue = deque()
        queue.append(K-1)
        on_q = [False] * N
        on_q[K-1] = True
        while queue:
            v = queue.popleft()
            on_q[v] = False
            for w, delay in graph[v]:
                if delay_to[w] > delay_to[v] + delay:
                    delay_to[w] = delay_to[v] + delay
                    if not on_q[w]:
                        queue.append(w)
        ans = max(delay_to)
        return -1 if ans == MAX else ans






def main():
    q = Q743()
    q.add_args([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    q.run()


if __name__ == "__main__":
    main()
