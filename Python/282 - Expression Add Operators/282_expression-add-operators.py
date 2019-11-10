from leezy import Solution, solution


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

    def addOperators_tle(self, num, target):
        if num == '':
            return []
        total = []
        self.dfs_tle(num, target, 0, '', total)
        return total

    def dfs_tle(self, nums, target, start, expr, total):
        if start == len(nums):
            if self.is_valid_soln(expr, target):
                total.append(expr)
            return
        cur_part = ''
        for i in range(start, len(nums)):
            cur_part += nums[i]
            if i > start and cur_part[0] == '0':
                break
            if i == len(nums) - 1:
                self.dfs_tle(nums, target, i+1, expr+cur_part, total)
            else:
                for op in '-+*':
                    self.dfs_tle(nums, target, i+1, expr+cur_part+op, total)

    def is_valid_soln(self, expr, target):
        return eval(expr) == target


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
