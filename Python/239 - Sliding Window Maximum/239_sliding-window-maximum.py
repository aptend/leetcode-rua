from leezy import solution, Solution

from collections import deque


class Q239(Solution):
    @solution
    def maxSlidingWindow(self, nums, k):
        q = deque()
        for x in range(k-1):
            while q and nums[q[-1]] < nums[x]:
                q.pop()
            q.append(x)
        ans = []
        for x in range(max(0, k-1), len(nums)):
            if q and q[0] <= x - k:
                q.popleft()
            while q and nums[q[-1]] < nums[x]:
                q.pop()
            q.append(x)
            ans.append(nums[q[0]])
        return ans

    @solution
    def max_sliding_window(self, A, k):
        q = deque()
        ans = []
        for i, x in enumerate(A):
            while q and A[q[-1]] < x:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                ans.append(A[q[0]])
        return ans


def main():
    q = Q239()
    q.add_case(q.case([1, 3, -1, -3, 5, 3, 6, 7], 3)
                .assert_equal([3, 3, 5, 5, 6, 7]))
    q.add_case(q.case([6, 5, 4, 3, 2, 1], 3)
                .assert_equal([6, 5, 4, 3]))
    q.add_case(q.case([1, 1, 1], 3).assert_equal([1]))
    q.add_case(q.case([7, 2, 4], 2).assert_equal([7, 4]))
    q.add_case(q.case([7, 2, 4], 2).assert_equal([7, 4]))
    q.add_case(q.case([1, 3, 1, 2, 0, 5], 3).assert_equal([3, 3, 2, 5]))
    q.add_case(q.case([], 0).assert_equal([]))
    q.add_case(q.case([1], 1).assert_equal([1]))
    q.run()


if __name__ == '__main__':
    main()
