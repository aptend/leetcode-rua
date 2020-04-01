from leezy import solution, Solution

#         1  2  3
# x       4  5  6
# ----------------
#            1  8
#         1  2
#         6
#         1  5
#      1  0
#      5
#      1  2
#      8
#   4
# ----------------
#   5  6  0  8  8


class Q043(Solution):
    @solution
    def multiply(self, num1, num2):
        n1 = [int(x) for x in num1[::-1]]
        n2 = [int(x) for x in num2[::-1]]
        ans = [0] * (len(n1) + len(n2) + 1)
        for i, a in enumerate(n1):
            for j, b in enumerate(n2):
                carry, x = divmod(a*b, 10)
                ans[i+j] += x
                ans[i+j+1] += carry
        for i in range(len(ans)-1):
            carry, x = divmod(ans[i], 10)
            ans[i] = x
            ans[i+1] += carry
        while ans and ans[-1] == 0:
            ans.pop()
        return '0' if not ans else ''.join(str(x) for x in ans[::-1])


def main():
    q = Q043()
    q.add_case(q.case('2', '3').assert_equal('6'))
    q.add_case(q.case('123', '456').assert_equal('56088'))
    q.add_case(q.case('100', '1').assert_equal('100'))
    q.add_case(q.case('0', '0').assert_equal('0'))
    q.run()


if __name__ == '__main__':
    main()

