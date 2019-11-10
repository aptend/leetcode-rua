from leezy import Solution, solution


class Q1186(Solution):
    @solution
    def maximumSum(self, arr):
        N = len(arr)
        MIN = float('-inf')
        start = [MIN] * (N+1)
        for i in range(N-1, -1, -1):
            if start[i+1] < 0:
                start[i] = arr[i]
            else:
                start[i] = arr[i] + start[i+1]
        end = [MIN] * (N+1)
        for i in range(N):
            if end[i-1] < 0:
                end[i] = arr[i]
            else:
                end[i] = arr[i] + end[i-1]
        
        ans = MIN
        for i in range(N):
            ans = max(ans, max(start[i+1]+end[i-1], end[i]+start[i]-arr[i]))
        return ans




def main():
    q = Q1186()
    q.add_args([1, -2, 0, 3])
    q.run()


if __name__ == "__main__":
    main()
