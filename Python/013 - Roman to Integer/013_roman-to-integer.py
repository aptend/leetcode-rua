from leezy import solution, Solution


class Q013(Solution):
    @solution
    def romanToInt(self, s):
        # 48ms 82.78%
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        N = len(s)
        ans = 0
        i = 0
        while i < N:
            ch = s[i]
            peek = '' if i == N-1 else s[i+1]
            if ch == 'I':
                if peek == 'V' or peek == 'X':
                    ans += table[peek] - 1
                    i += 1
                else:
                    ans += 1
            elif ch == 'X':
                if peek == 'L' or peek == 'C':
                    ans += table[peek] - 10
                    i += 1
                else:
                    ans += 10
            elif ch == 'C':
                if peek == 'D' or peek == 'M':
                    ans += table[peek] - 100
                    i += 1
                else:
                    ans += 100
            else:
                ans += table[ch]
            i += 1
        return ans


def main():
    q = Q013()
    q.add_case(q.case('III').assert_equal(3))
    q.add_case(q.case("IIII").assert_equal(4))
    q.add_case(q.case("IV").assert_equal(4))
    q.add_case(q.case("IX").assert_equal(9))
    q.add_case(q.case("IXII").assert_equal(11))
    q.add_case(q.case("LVIII").assert_equal(58))
    q.add_case(q.case("MCMXCIV").assert_equal(1994))
    q.run()

if __name__ == '__main__':
    main()
