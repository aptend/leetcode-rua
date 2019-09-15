from leeyzer import Solution, solution


class Q1130(Solution):
    @solution
    def mctFromLeafValues(self, arr):
        N = len(arr)
        memo = [[-1]*N for _ in range(N)]
        def construct(i, j):
            if i == j:
                return 0
            if memo[i][j] > 0:
                return memo[i][j]
            _min = float('inf')
            for k in range(i, j):
                left_min = construct(i, k)
                right_min = construct(k+1, j)
                _min = min(_min, left_min+right_min+max(arr[i:k+1])*max(arr[k+1:j+1]))
            memo[i][j] = _min
            return _min
        return construct(0, N - 1)

    @solution
    def mct_from_leaf_values(self, arr):
        # 20ms 83.47%
        # i have to say, this is...brainfucking and amazing!
        stack = []
        ans = 0
        for x in arr:
            while stack and stack[-1] < x:
                small = stack.pop()
                big = min(x, stack[-1]) if stack else x
                ans += big * small
            stack.append(x)
        for i in range(len(stack)-1, 0, -1):
            ans += stack[i] * stack[i-1]
        return ans



def main():
    q = Q1130()
    q.add_args([6, 2, 4])
    q.add_args([1, 2, 3, 4]) # 20
    q.add_args([1, 11, 3, 1, 5])  # 112
    q.add_args([6, 2, 11, 2, 13, 21, 6, 4, 1, 4]) # 686
    q.run()


if __name__ == "__main__":
    main()
