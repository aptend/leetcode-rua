from leezy import solution, Solution


class Q1031(Solution):
    @solution
    def maxSumTwoNoOverlap(self, A, L, M):
        # 52ms 81.28%
        N = len(A)
        def find_max(l, m):
            left_max = [0] * N
            win = sum(A[:l])
            max_ = win
            left_max[l-1] = max_
            for i in range(l, N-m):
                win += A[i] - A[i-l]
                max_= max(max_, win)
                left_max[i] = max_
            
            right_max = [0] * N
            win = sum(A[N-m:])
            max_ = win
            right_max[N-m] = max_
            for i in range(N-m-1, l-1, -1):
                win += A[i] - A[i+m]
                max_= max(max_, win)
                right_max[i] = max_

            ans = 0
            for i in range(l-1, N-m):
                ans = max(ans, left_max[i] + right_max[i+1])
            return ans
        return max(find_max(L, M), find_max(M, L))



def main():
    q = Q1031()
    q.add_case(q.case([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2).assert_equal(20))
    q.add_case(q.case([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2).assert_equal(29))
    q.add_case(q.case([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3).assert_equal(31))
    q.run()

if __name__ == '__main__':
    main()
