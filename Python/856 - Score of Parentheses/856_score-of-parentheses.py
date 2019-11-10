from leezy import Solution, solution


class Q856(Solution):
    @solution
    def scoreOfParentheses(self, S):
        def score(i, j):
            # 16ms 82.0%
            if S[i:j+1] == '()':
                return 1
            # assert S[i] == '('  balanced input
            open_ = 1
            for r in range(i+1, j):
                if S[r] == '(':
                    open_ += 1
                else:
                    open_ -= 1
                if open_ == 0: # balanced substring
                    return score(i, r) + score(r+1, j)
            # assert open_ = 1 full balanced
            return 2 * score(i+1, j-1)
        return score(0, len(S)-1)
    
    @solution
    def score_parentheses(self, S):
        # 20ms
        stack = [0]
        for i in range(1, len(S)):
            if S[i] == '(':
                if S[i-1] == '(':
                    stack.append(0)
            else:
                if S[i-1] == '(':
                    score = 1
                else:
                    score = stack.pop() * 2
                stack.append(stack.pop() + score)
        return stack[0]


def main():
    q = Q856()
    q.add_args('()')
    q.add_args('(())')
    q.add_args('()()')
    q.add_args('(()(()))')
    q.run()


if __name__ == "__main__":
    main()
