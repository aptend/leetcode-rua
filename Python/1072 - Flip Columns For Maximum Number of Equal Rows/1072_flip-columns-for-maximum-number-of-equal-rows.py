from leezy import solution, Solution
from collections import defaultdict

class Q1072(Solution):
    @solution
    def maxEqualRowsAfterFlips(self, matrix):
        # 1988ms 27.14%
        table = defaultdict(int)
        for row in matrix:
            table[''.join(str(x) for x in row)] += 1
            table[''.join(str(1-x) for x in row)] += 1
        return max(table.values())



def main():
    q = Q1072()
    q.add_case(q.case([[0, 1], [1, 1]]).assert_equal(1))
    q.add_case(q.case([[0, 1], [1, 0]]).assert_equal(2))
    q.add_case(q.case([[0, 0, 0], [0, 0, 1], [1, 1, 0]]).assert_equal(2))
    q.run()

if __name__ == '__main__':
    main()
