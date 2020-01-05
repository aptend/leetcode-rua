from leezy import solution, Solution


class Q012(Solution):
    @solution
    def intToRoman(self, num):
        # 56ms 24.7%
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbls = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans = []
        while num > 0:
            for v, s in zip(vals, symbls):
                if v <= num:
                    num -= v
                    ans.append(s)
                    break

        return ''.join(ans)
    
    @solution
    def int_to_roman(self, num):
        # 56ms 24.7%
        vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbls = ['I', 'IV', 'V', 'IX', 'X', 'XL',
                  'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        ans = []
        while num > 0:
            for v, s in zip(vals[::-1], symbls[::-1]):
                if v <= num:
                    num -= v
                    ans.append(s)
                    break
                else:
                    vals.pop()
                    symbls.pop()
        return ''.join(ans)


def main():
    q = Q012()
    q.add_case(q.case(3).assert_equal('III'))
    q.add_case(q.case(4).assert_equal('IV'))
    q.add_case(q.case(9).assert_equal('IX'))
    q.add_case(q.case(58).assert_equal('LVIII'))
    q.add_case(q.case(1994).assert_equal('MCMXCIV'))
    q.run()


if __name__ == '__main__':
    main()
