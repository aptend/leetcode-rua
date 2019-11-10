from leezy import solution, Solution

class Q962(Solution):
    @solution
    def maxWidthRamp(self, A):
        # 560ms 20%
        stack = []
        def bisect(stack, x):
            i, j = 0, len(stack)-1
            while i <= j:
                mid = i + (j-i) // 2
                if A[stack[mid]] <= x:
                    j = mid - 1
                else:
                    i = mid + 1
            # we can index i safely, because A[stack[-1]] <= a
            return stack[i]
        ans = 0
        for i, a in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
            else:
                idx = i - bisect(stack, a)
                ans = max(ans, idx)
        return ans

    @solution
    def max_width_ramp(self, A):
        # 360ms
        # lee215 rocks
        stack = []
        ans = 0
        for i, a in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
        for j in reversed(range(len(A))):
            while stack and A[stack[-1]] <= A[j]:
                ans = max(ans, j - stack.pop())
        return ans


def main():
    q = Q962()
    q.add_args([6, 0, 8, 2, 1, 5])
    q.add_args([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
    q.run()

if __name__ == '__main__':
    main()
