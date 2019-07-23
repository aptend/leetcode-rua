from leeyzer import Solution, solution


class Q282(Solution):
    @solution
    def addOperators(self, num, target):
        # 792ms 82.73%
        # using 227 basic-calculator-ii
        total = []
        def dfs(start, val, accum, expr):
            if start == len(num):
                if val + accum == target:
                    total.append(expr)
                return
            x = 0
            str_x = ''
            for i in range(start, len(num)):
                if i > start and num[start] == '0':
                    break
                x = 10 * x + int(num[i])
                str_x += num[i]
                if start == 0:
                    dfs(i+1, val+accum, x, expr+str_x)
                else:
                    dfs(i+1, val+accum, x, expr+'+'+str_x)
                    dfs(i+1, val+accum, -x, expr+'-'+str_x)
                    dfs(i+1, val, accum*x, expr+'*'+str_x)
        dfs(0, 0, 0, '')
        return total


def main():
    q = Q282()
    q.add_args('123', 6)
    q.add_args('123', 123)
    q.add_args('232', 8)
    q.add_args('105', 5)
    q.add_args('00', 0)
    q.add_args('3456237490', 3456237490)
    q.run()


if __name__ == "__main__":
    main()
