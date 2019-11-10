from leezy import Solution, solution



"""

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass

Comments from lxnn:
To make the intuition a bit more concrete: why is it that we can make the string valid with the fewest additions by adding some ( on the left and some ) on the right?

The key fact is that, given a valid parenthetical string, we can pick any ')' and move it all the way to the right end, or any ( and move it all the way to the left end, without invalidating the string. So given a fewest-additions answer, we can take the parentheses we added and move them to the ends, for an equally valid answer. 



which means, in this method, we try our best to find those parens that formed valid parens

and it's safe to move mismatched left parens to right end and mismatched parens to the left end.

the number of parens needed to complete those mismatched end parens is the answer and the smallest answer
"""

class Q921(Solution):
    @solution
    def minAddToMakeValid(self, S):
        # 301 - Remove Invalid Parentheses
        left = right = 0
        for c in S:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right


def main():
    q = Q921()
    q.add_args('())')
    q.add_args('()))((')
    q.run()


if __name__ == "__main__":
    main()
