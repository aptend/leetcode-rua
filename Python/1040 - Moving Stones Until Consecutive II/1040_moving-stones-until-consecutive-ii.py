from leezy import solution, Solution


class Q1040(Solution):
    @solution
    def numMovesStonesII(self, stones):
        # hard
        N = len(stones)
        S = sorted(stones)
        min_shrink_by_first_move = min(S[N-1]-S[N-2], S[1]-S[0]) - 1
        max_s = S[N-1] - S[0] + 1 - N - min_shrink_by_first_move
        min_s = float('inf')
        i = 0
        for j in range(0, N):
            while S[j] - S[i] >= N:
                i += 1
            if j - i + 1 == N - 1 and S[j] - S[i] == N - 2:
                min_s = min(min_s, 2)
            else:
                min_s = min(min_s, N - (j - i + 1))
        return [min_s, max_s]

def main():
    q = Q1040()
    q.add_case(q.case([7, 4, 9]).assert_equal([1, 2]))
    q.add_case(q.case([6, 5, 4, 3, 10]).assert_equal([2, 3]))
    q.add_case(q.case([100, 101, 104, 102, 103]).assert_equal([0, 0]))
    q.add_case(q.case([1, 3, 6, 9]).assert_equal([2, 4]))
    q.run()

if __name__ == '__main__':
    main()
