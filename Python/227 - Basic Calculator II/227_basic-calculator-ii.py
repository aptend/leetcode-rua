from leezy import solution, Solution


class Q227(Solution):
    @solution
    def calculate(self, s):
        # 80ms 95.36%
        num = ''
        block = 0
        total = 0
        op = None
        flag = 1

        def calc_block(prev_op, cur_num, block):
            x = int(cur_num)
            if prev_op is None: # first operand
                return x
            elif prev_op == '/':
                return block // x
            elif prev_op == '*':
                return block * x

        for ch in s+'+':
            if ch == ' ':
                continue
            elif ch == '+' or ch == '-': # increase / decrease total
                x = int(num)
                if op is not None: # there was a block, do the last calc
                    if op == '/':
                        total += flag * (block // x)
                    elif op == '*':
                        total += flag * block * x
                else:
                    total += flag * x
                flag = 1 if ch == '+' else -1
                block = 0
                num = ''
                op = None
            elif ch == '/' or ch == '*':
                block = calc_block(op, num, block)
                num = ''
                op = ch
            else:
                num += ch
        return total
    

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
