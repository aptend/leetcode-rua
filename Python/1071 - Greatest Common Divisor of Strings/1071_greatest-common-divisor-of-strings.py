from leezy import solution, Solution


class Q1071(Solution):
    @solution
    def gcdOfStrings(self, str1, str2):
        # 28ms 88.13%
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        N = len(str1)
        for i in range(N, 0, -1):
            if N % i != 0:
                continue
            s = str1[:i]
            if all(x == '' for x in str1.split(s)) and all(x == '' for x in str2.split(s)):
                return s
        return ''


def main():
    q = Q1071()
    q.add_case(q.case('ABCABC', 'ABC').assert_equal('ABC'))
    q.add_case(q.case('LEET', 'CODE').assert_equal(''))
    q.run()

if __name__ == '__main__':
    main()
