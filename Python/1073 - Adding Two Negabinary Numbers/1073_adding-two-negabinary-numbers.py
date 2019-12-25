from leezy import solution, Solution
from itertools import zip_longest

class Q1073(Solution):
    @solution
    def addNegabinary(self, arr1, arr2):
        # 64ms 78.36%
        ans = []
        carry = 0
        for a, b in zip_longest(arr1[::-1], arr2[::-1], fillvalue=0):
            x = a + b + carry
            if x == -1:
                carry = 1
            elif x >= 2:
                carry = -1
            else:
                carry = 0
            ans.append(abs(x) % 2)
        
        if carry == -1:
            ans.extend([1, 1])
        elif carry == 1:
            ans.append(1)
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]




def main():
    q = Q1073()
    q.add_case(q.case([1, 0, 1], [1, 0, 1]).assert_equal([1,1,1,1,0]))
    q.add_case(q.case([1, 1, 1, 1, 1], [1, 0, 1]).assert_equal([1,0,0,0,0]))
    q.add_case(q.case([1], [1]).assert_equal([1,1,0]))
    q.add_case(q.case([1], [1, 0, 1]).assert_equal([1,1,0,1,0]))
    q.add_case(q.case([1], [1, 1]).assert_equal([0]))
    q.run()

if __name__ == '__main__':
    main()
