from leeyzer import Solution, solution


class Q1190(Solution):
    @solution
    def reverseParentheses(self, s):
        # 32ms 95.88%
        stack = [[]]
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                inner = stack.pop()
                stack[-1].extend(inner[::-1])
            else:
                stack[-1].append(ch)
        return ''.join(stack[-1])

    @solution
    def reverse_parentheses(self, s):
        # 36ms 85.67%
        pairs = []
        open_ = 0
        l = 0
        # find all outtest parentheses
        # '()((42))' -> [[0, 1], [2, 7]]
        for i, ch in enumerate(s):
            if ch == '(':
                open_ += 1
                if open_ == 1:
                    l = i
            elif ch == ')':
                open_ -= 1
                if open_ == 0:
                    pairs.append([l, i])
        if len(pairs) == 0:
            return s
        ans = ''
        prev = 0
        for l, r in pairs:
            ans += s[prev:l]
            ans += self.reverse_parentheses(s[l+1:r])[::-1]
            prev = r+1
        ans += s[prev:]
        return ans

def main():
    q = Q1190()
    q.add_args('(abcd)')
    q.add_args('(u(love)i)')
    q.add_args('(ed(et(oc))el)')
    q.add_args('a(bcdefghijkl(mno)p)q')
    q.run()


if __name__ == "__main__":
    main()
