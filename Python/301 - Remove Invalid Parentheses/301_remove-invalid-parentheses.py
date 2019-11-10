from leezy import Solution, solution


class Q301(Solution):
    @solution
    def removeInvalidParentheses(self, s):
        # the solution for 921 - Minimum Add to Make Parentheses Valid
        # according to the proof of 921, 
        # it's easy to kown minimum add == minimum delete
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        total = set()
        self.dfs(s, 0, '', 0, left, right, total)
        return list(total)
    
    def dfs(self, s, i, formed, open, left, right, total):
        """
        :s: original input string  
        :i: handle char s[i], pick or ignore?  
        :formed: chars have been picked so far  
        :open: how many dangling '(' in the `formed` string  
        :left: how many '(' planned to be removed  
        :right: how many ')' planned to be removed  
        :total: result set  
        """
        if i == len(s):
            if left == 0 and right == 0 and open == 0:
                total.add(formed)
            return
        c = s[i]
        if c == ')':
            if open > 0: # just pick
                self.dfs(s, i+1, formed+')', open-1, left, right, total)
            if right > 0:
                self.dfs(s, i+1, formed, open, left, right-1, total)
        elif c == '(':
            self.dfs(s, i+1, formed+'(', open+1, left, right, total)
            if left > 0:
                self.dfs(s, i+1, formed, open, left-1, right, total)
        else:
            self.dfs(s, i+1, formed+c, open, left, right, total)






def main():
    q = Q301()
    q.add_args('()())()')
    q.add_args("(a)())()")
    q.add_args("((())()")
    q.add_args("()(())()")
    q.add_args(")(f")
    q.run()


if __name__ == "__main__":
    main()
