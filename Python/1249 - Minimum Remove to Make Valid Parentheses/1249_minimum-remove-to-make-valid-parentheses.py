from leezy import solution, Solution

class Q1249(Solution):
    @solution
    def minRemoveToMakeValid(self, s):
        # 132ms 78.89%
        # proof can be found in 301
        s = list(s)
        open_at = []
        for i, ch in enumerate(s):
            if ch == '(':
                open_at.append(i)
            elif ch == ')':
                if len(open_at) == 0:
                    s[i] = '_'
                else:
                    open_at.pop()
        for i in open_at:
            s[i] = '_'
        return ''.join(ch for ch in s if ch != '_')



def main():
    q = Q1249()
    q.add_args('lee(t(c)o)de)')
    q.run()

if __name__ == '__main__':
    main()
