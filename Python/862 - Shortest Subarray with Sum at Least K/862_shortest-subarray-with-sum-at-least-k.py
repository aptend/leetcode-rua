from leezy import Solution, solution

from collections import deque

"""
A = [2, -1, 2, 1]  K = 3

B = [0, 2, 1, 3, 4]
B[i] - B[j] >= K   given i, want nearest j

maintain an increasing queue
q = [0] -> [0, 1] -> [0, 2] -> [2, 3] -> [3, 4]

This problem is awesome
"""

class Q862(Solution):
    @solution
    def shortestSubarray(self, A, K):
        # 746ms 96.71%
        N = len(A)
        B = [0] * (N + 1)
        # prefix sum
        for i, x in enumerate(A, 1):
            B[i] = B[i-1] + x
        # q holds every candidate of start idx of the final subarray
        q = deque()
        ans = N + 1
        for i in range(N+1):
            while q and B[i] - B[q[0]] >= K:
                ans = min(ans, i-q.popleft())
            # this is the basic operation to maintain a monotonic queue
            while q and B[q[-1]] >= B[i]:
                # we don't need to consider this index any more
                q.pop()
            q.append(i)
        return ans if ans < N + 1 else -1


def main():
    q = Q862()
    q.add_args([1], 1)
    q.add_args([2, -1, 2, 1], 3)
    q.run()


if __name__ == "__main__":
    main()
