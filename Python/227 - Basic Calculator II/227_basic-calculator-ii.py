from leezy import solution, Solution


class Q227(Solution):
    @solution
    def calculate(self, s):
        # 80ms 95.36%
        num = 0
        block = 0
        ans = 0
        prev_op = '+'
        for ch in s+'+':
            if ch == ' ':
                continue
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:  # + - * /
                if prev_op == '+':
                    block += num
                elif prev_op == '-':
                    block -= num
                elif prev_op == '*':
                    block *= num
                else:
                    if block < 0:
                        block = -(-block // num)
                    else:
                        block //= num
                if ch == '+' or ch == '-':
                    ans += block
                    block = 0
                num = 0
                prev_op = ch
        return ans

    def parse(self, expr):
        tokens = []
        nums = ""
        for ch in expr:
            if ch == " ":
                continue
            elif ch in '+-*/':
                if nums:
                    tokens.append(nums)
                    nums = ""
                tokens.append(ch)
            else:
                nums += ch
        if nums:
            tokens.append(nums)
        return tokens

    @solution
    def calc(self, s):
        tokens = self.parse(s)
        total = 0
        accum = int(tokens[0])
        i = 1
        while i < len(tokens):
            op = tokens[i]
            if op in '+-':
                total += accum
                i += 1
                accum = int(tokens[i])
                if op == '-':
                    accum *= -1
            else:
                i += 1
                n = int(tokens[i])
                if op == "*":
                    accum *= n
                else:
                    if accum > 0:
                        accum //= n
                    else:
                        accum = -(accum // (-n))
            i += 1
        return total + accum


def main():
    q = Q227()
    q.add_case(q.case('14 - 3/2').assert_equal(13))
    q.add_case(q.case('3+2*2').assert_equal(7))
    q.add_case(q.case('3/2 ').assert_equal(1))
    q.add_case(q.case('3+5 / 2 ').assert_equal(5))
    q.run()


if __name__ == '__main__':
    main()
