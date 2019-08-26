from leeyzer import Solution, solution


class Q907(Solution):
    """Ref to 84. Largest Rectangle in Histogram
    """
    @solution
    def sumSubarrayMins(self, A):
        # 508ms 44.17%
        N = len(A)
        stack = []
        left = [0] * N
        for i in range(N):
            while stack and A[stack[-1]] >= A[i]: # note ge
                stack.pop()
            left[i] = i - stack[-1] - 1 if stack else i
            stack.append(i)
        stack = []
        right = [0] * N
        for i in range(N-1, -1, -1):
            while stack and A[stack[-1]] > A[i]: # note gt
                stack.pop()
            right[i] = stack[-1] - i - 1 if stack else N-1-i
            stack.append(i)
        kmod = 10 ** 9 + 7
        ans = 0
        for i, x in enumerate(A):
            ans = (ans + x * (left[i]+1) * (right[i]+1)) % kmod
        return ans
    
    @solution
    def sum_subarray_mins(self, A):
        # 408ms 76.18%
        kmod = 10 ** 9 + 7
        ans = 0
        A = A + [0]
        stack = [-1]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                j = stack.pop()
                cnt = (i - j) * (j - stack[-1])
                ans = (ans + A[j] * cnt) % kmod
            stack.append(i)
        return ans




def main():
    q = Q907()
    q.add_args([3, 1, 2, 4])
    q.add_args([71, 55, 82, 55]) # 593
    q.run()


if __name__ == "__main__":
    main()
