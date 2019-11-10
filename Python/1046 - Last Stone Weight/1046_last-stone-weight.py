from leezy import Solution, solution

from heapq import heapify, heappop, heappush
class Q1046(Solution):
    @solution
    def lastStoneWeight(self, stones):
        # 12ms 96.55% / 36ms
        heap = [-x for x in stones]
        heapify(heap)
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y:
                heappush(heap, x-y)
        return -heap[0] if heap else 0


def main():
    q = Q1046()
    q.add_args([2, 7, 4, 1, 8, 1])
    q.run()


if __name__ == "__main__":
    main()
