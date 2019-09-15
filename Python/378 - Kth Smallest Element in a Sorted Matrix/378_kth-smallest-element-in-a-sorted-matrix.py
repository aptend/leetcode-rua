from leeyzer import Solution, solution

from heapq import heappop, heappush
from bisect import bisect_right

class Q378(Solution):
    @solution
    def kthSmallest(self, matrix, k):
        # nlog(n)*log(max-min) 140ms 98.05%
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            m = lo + (hi - lo) // 2
            le = 0
            for row in matrix:
                le += bisect_right(row, m)
            if le >= k:
                hi = m - 1
            else:
                lo = m + 1
        return lo
    
    @solution
    def kth_smallest_prune(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            m = lo + (hi - lo) // 2
            le = 0
            for row in matrix:
                le += bisect_right(row, m)
                if le == 0 or le >= k:
                    break
            if le >= k:
                hi = m - 1
            else:
                lo = m + 1
        return lo

    @solution
    def kth_smallest_On(self, matrix, k):
        # n*log(max-min) 136ms 99.47% / 144ms
        lo, hi = matrix[0][0], matrix[-1][-1]
        N = len(matrix)
        while lo <= hi:
            m = lo + (hi - lo) // 2
            le = 0
            i, j = 0, N-1
            for i in range(N):
                while j >= 0 and matrix[i][j] > m:
                    j -= 1
                if j == -1:
                    break
                le += j+1
            if le >= k:
                hi = m - 1
            else:
                lo = m + 1
        return lo

    @solution
    def kth_smallest_heap(self, matrix, k):
        N = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        def push(i, j):
            if i < N and j < N:
                heappush(heap, (matrix[i][j], i, j))
        for _ in range(k):
            ans, i, j = heappop(heap)
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return ans



def main():
    q = Q378()
    M = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    q.add_args(M, 1)
    q.add_args(M, 2)
    q.add_args(M, 8)
    q.add_args(M, 9)
    q.run()


if __name__ == "__main__":
    main()
