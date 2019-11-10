from leezy import solution, Solution

class Q008(Solution):
    @solution
    def myAtoi(self, str):
        # 44ms 47%
        s = str.strip()
        if len(s) == 0:
            return 0
        ans = 0
        flag = 1
        ch = s[0]
        if ch == '-':
            flag = -1
        elif ch.isdigit():
            ans = int(ch)
        elif ch != '+':
            return 0
        
        MAX, MIN = 2 ** 31 - 1, -(2 ** 31)
        M = MAX // 10
        for ch in s[1:]:
            if ch.isdigit():
                d = int(ch)
                if ans > M or (ans == M and d > 7):
                    return MAX if flag > 0 else MIN
                ans = 10 * ans + d
            else:
                break
        return flag * ans
    


def main():
    q = Q008()
    q.add_args('42')
    q.add_args('++42')
    q.add_args("xx")
    q.add_args("")
    q.add_args("+0")
    q.add_args("-0")
    q.add_args("42")
    q.add_args("+42")
    q.add_args("   -42")
    q.add_args("  - 42")
    q.add_args("0000000000000000003")
    q.add_args("  +4396 famous  ")
    q.add_args("2147483648")
    q.add_args("2147483638")
    q.add_args("11474836381")
    q.add_args("-11474836481")
    q.add_args("-2147483648")
    q.run()

if __name__ == '__main__':
    main()

