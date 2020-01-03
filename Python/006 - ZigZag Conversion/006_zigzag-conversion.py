from leezy import solution, Solution
from itertools import cycle

class Q006(Solution):
    @solution
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = []
        total_span = 2 * (numRows - 1)
        for i in range(numRows):
            j = i
            sp1 = total_span - i * 2
            sp2 = total_span - sp1
            for gap in cycle([sp1, sp2]):
                if gap == 0:
                    continue
                if j >= len(s):
                    break
                ans.append(s[j])
                j += gap
        return ''.join(ans)


def main():
    q = Q006()
    q.add_case(q.case('PAYPALISHIRING', 4).assert_equal("PINALSIGYAHRPI"))
    q.add_case(q.case('PAYPALISHIRING', 3).assert_equal("PAHNAPLSIIGYIR"))
    q.run()

if __name__ == '__main__':
    main()
