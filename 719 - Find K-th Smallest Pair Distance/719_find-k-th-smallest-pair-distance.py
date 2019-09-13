from leeyzer import Solution, solution
from heapq import heappush, heappop

class Q719(Solution):
    @solution
    def smallestDistancePair(self, nums, k):
        # MLE
        A = sorted(nums)
        N = len(A)
        heap = []

        def push(i, j):
            heappush(heap, (abs(A[i]-A[j]), i, j))
        for i in range(N-1):
            push(i, i+1)
        for _ in range(k):
            ans, i, j = heappop(heap)
            if j < N-1:
                push(i, j+1)
        return ans



def main():
    q = Q719()
    q.add_args([1, 3, 1], 1)
    q.run()


if __name__ == "__main__":
    main()
