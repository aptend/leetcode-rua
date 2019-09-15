from leeyzer import Solution, solution


class Q1047(Solution):
    @solution
    def removeDuplicates(self, S):
        # TLE tests past 87/98
        def solve(s):
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    return solve(s[:i]+s[i+2:])
            return s
        return solve(S)
    
    @solution
    def remove_duplicate(self, S):
        # 52ms 99.22%
        ans = ['']
        for ch in S:
            if ans[-1] == ch:
                ans.pop()
            else:
                ans.append(ch)
        return ''.join(ans)

def main():
    q = Q1047()
    q.add_args('abbaca')
    q.add_args('cabbaca')
    q.add_args('cabbbaca')
    q.run()


if __name__ == "__main__":
    main()
