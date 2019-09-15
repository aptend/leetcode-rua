from leeyzer import Solution, solution
import re
from operator import add, sub, mul

class Q241(Solution):
    @solution
    def diffWaysToCompute(self, input):
        # 16ms 96.13%
        parts = re.split(r'([-+*])', input)
        memo = {}
        return self.ways(parts, memo, 0, len(parts)-1)

    def ways(self, parts, memo, lo, hi):
        if (lo, hi) in memo:
            return memo[(lo, hi)]
        if lo == hi:
            return [int(parts[lo])]
        res = []
        for i in range(lo+1, hi, 2):
            if parts[i] == '+':
                op = add
            elif parts[i] == '-':
                op = sub
            elif parts[i] == '*':
                op = mul
            else:
                raise RuntimeError(f'unrecognized op {parts[i]!r}')
            left = self.ways(parts, memo, lo, i-1)
            right = self.ways(parts, memo, i+1, hi)
            for l in left:
                for r in right:
                    res.append(op(l, r))
        memo[(lo, hi)] = res
        return res



def main():
    q = Q241()
    q.add_args('2-1-1')
    q.add_args('2*3-4*5')
    q.run()


if __name__ == "__main__":
    main()
