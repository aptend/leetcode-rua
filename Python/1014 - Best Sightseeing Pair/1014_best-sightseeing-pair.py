from leezy import solution, Solution


class Q1014(Solution):
    @solution
    def maxScoreSightseeingPair(self, A):
        # 528ms 75.80%
        candi = A[0]
        ans = 0
        for i, a in enumerate(A[1:], 1):
            ans = max(ans, candi + a - i)
            candi = max(candi, a + i)
        return ans


def main():
    q = Q1014()
    q.add_case(q.case([8, 1, 5, 2, 6]))
    q.run()

if __name__ == '__main__':
    main()
