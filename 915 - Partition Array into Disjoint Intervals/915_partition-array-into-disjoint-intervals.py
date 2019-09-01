from leeyzer import Solution, solution


class Q915(Solution):
    @solution
    def partitionDisjoint(self, A):
        # 188ms 44.33%
        N = len(A)
        maximum = [A[0]] * N
        minimum = [A[-1]] * N
        max_ = A[0]
        min_ = A[-1]
        for i in range(N):
            j = N-1-i
            max_ = max(max_, A[i])
            min_ = min(min_, A[j])
            maximum[i] = max_
            minimum[j] = min_
        for i in range(N):
            # omit edge cases checking because
            # it is guaranteed that there is one solution
            if maximum[i] <= minimum[i+1]:
                return i + 1




def main():
    q = Q915()
    q.add_args([5, 0, 3, 8, 6])
    q.add_args([1, 1, 1, 0, 6, 12])
    q.run()


if __name__ == "__main__":
    main()
