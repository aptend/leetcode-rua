from leezy import solution, Solution


class Q1021(Solution):
    @solution
    def removeOuterParentheses(self, S):
        i = 0
        left = 0
        ans = ''
        for (j, ch) in enumerate(S):
            if ch == '(':
                left += 1
            else:
                left -= 1
                if left == 0:
                    ans += S[i+1:j]
                    i = j+1
        return ans


def main():
    q = Q1021()
    q.add_case(q.case('(()())(())').assert_equal('()()()'))
    q.run()

if __name__ == '__main__':
    main()
