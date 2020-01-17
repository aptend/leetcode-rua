from leezy import solution, Solution


class Q224(Solution):
    @solution
    def calculate(self, s):
        # 104ms 57.50%
        s = '(' + s + ')'
        N = len(s)

        # calc 只会在(后一个字符处调用，遇到第一个)就是当前一层calc结束
        def calc(lo):
            stack = []
            num = 0
            prev_op = '+'
            i = lo
            while i < N:
                ch = s[i]
                if ch == '(':
                    num, i = calc(i+1)
                elif ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch != ' ':  # + - * / )
                    if prev_op == '+':
                        stack.append(num)
                    elif prev_op == '-':
                        stack.append(-num)
                    elif prev_op == '*':
                        stack.append(stack.pop() * num)
                    elif prev_op == '/':
                        div = stack.pop()
                        if div < 0:
                            stack.append(-(-div // num))
                        else:
                            stack.append(div // num)
                    if ch == ')':
                        return sum(stack), i
                    num = 0
                    prev_op = ch
                i += 1
            raise ValueError('unbalanced parentheses')

        ans, _handled_n = calc(1)
        return ans

    @solution
    def calculate_without_stack(self, s):
        s = '(' + s + ')'
        N = len(s)

        def calc(lo):
            ans = 0
            block = 0
            num = 0
            prev_op = '+'
            i = lo
            while i < N:
                ch = s[i]
                if ch == '(':
                    num, i = calc(i+1)
                elif ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch != ' ':  # + - * / )
                    if prev_op == '+':
                        block += num
                    elif prev_op == '-':
                        block -= num
                    elif prev_op == '*':
                        block *= num
                    elif prev_op == '/':
                        if block < 0:
                            block = -(-block // num)
                        else:
                            block = block // num
                    if ch == '+' or ch == '-':
                        ans += block
                        block = 0
                    if ch == ')':
                        return ans + block, i
                    num = 0
                    prev_op = ch
                i += 1
            raise ValueError('unbalanced parentheses')

        ans, _handled_n = calc(1)
        return ans


def main():
    q = Q224()
    q.add_case(q.case('0').assert_equal(0))
    q.add_case(q.case('1 + 2*3/6').assert_equal(2))
    q.add_case(q.case('(1 + 2)*3/6').assert_equal(1))
    q.add_case(q.case('(1 - 2)*3/6').assert_equal(0))
    q.add_case(q.case('1 + 1').assert_equal(2))
    q.add_case(q.case('2-1 + 2').assert_equal(3))
    q.add_case(q.case('(1+(4+5+2)-3)+(6+8)').assert_equal(23))
    q.run()


if __name__ == '__main__':
    main()
