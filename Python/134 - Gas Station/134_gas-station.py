from leezy import solution, Solution

from itertools import chain

class Q134(Solution):
    @solution
    def canCompleteCircuit(self, gas, cost):
        # 48ms 98.00%
        # O(n) consider this problem in a line graph with translation
        s = 0
        min_s = float('inf')
        idx = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            s += g - c
            if s < min_s:
                min_s = s
                idx = i
        if s < 0:
            return -1
        if idx == len(gas) - 1:
            return 0
        else:
            return idx + 1
        
    @solution
    def can_complete(self, gas, cost):
        # 1284ms 7%
        # O(n^2)
        incomes = [g-c for g, c in zip(gas, cost)]
        for idx, income in enumerate(incomes):
            if income >= 0:
                for next_income in chain(incomes[idx+1:], incomes[:idx]):
                    income += next_income
                    if income < 0:
                        break
                else:
                    return idx
        return -1



def main():
    q = Q134()
    q.add_case(q.case([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]).assert_equal(3))
    q.add_case(q.case([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]).assert_equal(4))
    q.add_case(q.case([3, 3, 4], [3, 4, 4]).assert_equal(-1))
    q.run()

if __name__ == '__main__':
    main()
