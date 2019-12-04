from leezy import solution, Solution


class Q032(Solution):
    @solution
    def longestValidParentheses(self, s):
        # 44ms 88.51%
        ans = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()  # paired paren
                if not stack:
                    stack.append(i) # ensure len(stack) >= 1
                # s[stack[-1]+1..=i] is a valid paren string
                else:
                    ans = max(ans, i - stack[-1])
        return ans
    
    @solution
    def longest_valid_parentheses(self, s):
        # 44ms
        if not s:
            return 0
        dp = [0] * len(s)
        for i, ch in enumerate(s):
            if ch == '(':
                continue
            if i-1 >= 0 and i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
        return max(dp)


def main():
    q = Q032()
    q.add_case(q.case('(()').assert_equal(2))
    q.add_case(q.case('((())').assert_equal(4))
    q.add_case(q.case(')()())').assert_equal(4))
    q.add_case(q.case('(()(()').assert_equal(2))
    q.add_case(q.case(')))(((').assert_equal(0))
    q.add_case(q.case('(()))())(').assert_equal(4))

    q.run()

if __name__ == '__main__':
    main()
