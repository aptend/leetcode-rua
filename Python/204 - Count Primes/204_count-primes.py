from leezy import Solution, solution

import math


class Q204(Solution):
    @solution
    def countPrimes(self, n):
        # 480ms 66.00%
        p_map = [True] * n
        for i in range(2, int(math.sqrt(n))+1):
            if not p_map[i]:
                continue
            for j in range(i*i, n, i):
                p_map[j] = False
        return len([i for i in range(2, n) if p_map[i]])



def main():
    q = Q204()
    q.add_args(10)
    q.add_args(0)
    q.add_args(1)
    q.add_args(5)
    q.run()


if __name__ == "__main__":
    main()
