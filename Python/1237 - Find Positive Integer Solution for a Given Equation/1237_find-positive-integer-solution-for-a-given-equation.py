
from leeyzer import solution, Solution

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
           pass
"""
class Q1237(Solution):

    @solution
    def findSolution(self, customfunction, z):
        # 56ms
        # naive solution matches its easy level
        ans = []
        for i in range(1, 1001):
            for j in range(1, 1001):
                x = customfunction.f(i, j)
                if x == z:
                    ans.append([i, j])
                elif x > z:
                    break
        return ans

    @solution
    def find_solution(self, container, z):
        # 252ms
        # binary search is better, in theory
        ans = []
        for i in range(1, 1001):
            lo, hi = 1, 1000
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                x = container.f(i, mid)
                if x == z:
                    ans.append([i, mid])
                    break
                elif x > z:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return ans


class Function:
    def __init__(self, func):
        self.f = func

def main():
    q = Q1237()
    q.add_args(Function(lambda x, y: x + y), 5)
    q.add_args(Function(lambda x, y: x * y), 5)
    q.run()


if __name__ == '__main__':
    main()
