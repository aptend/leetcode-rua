from leeyzer import Solution, solution
from collections import Counter, defaultdict

class Q1178(Solution):
    @solution
    def findNumOfValidWords(self, words, puzzles):
        # 1512ms 21.46%
        ws = Counter(''.join(sorted(set(w))) for w in words)
        def dfs(s, start, curr, total):
            if start >= len(s):
                return
            total.append(''.join(curr))
            for i in range(start, len(s)):
                curr.append(s[i])
                dfs(s, i + 1, curr, total)
                curr.pop()
        ans = []
        for p in puzzles:
            gem = p[0]
            pzz = sorted(p)
            cur, total = [], []
            dfs(pzz, 0, cur, total)
            cnt = 0
            for pat in [p for p in total[1:] if gem in p]:
                cnt += ws[pat]
            ans.append(cnt)
        return ans

    @solution
    def valid_words(self, words, puzzles):
        # 524ms 98.71%
        base = ord('a')
        mods = defaultdict(int)
        for w in words:
            bit_state = 0
            for ch in w:
                bit_state |= 1 << (ord(ch) - base)
            mods[bit_state] += 1
        
        ans = []
        for p in puzzles:
            h_st = 1 << (ord(p[0]) - base)
            r_st = 0
            for ch in p:
                r_st |= 1 << (ord(ch) - base)
            st = r_st
            cnt = 0
            while st:
                # if first letter in the pattern
                if st & h_st:
                    cnt += mods[st]
                # the most tricky part:
                # generate all subsets containing '1'
                st = (st - 1) & r_st
            ans.append(cnt)
        return ans



def main():
    q = Q1178()
    q.add_args(['aaaa', 'asas', 'able', 'ability', 'actt', 'actor', 'access'], ['aboveyz', 'abrodyz', 'abslute', 'absoryz', 'actresz', 'gaswxyz'])
    q.run()


if __name__ == "__main__":
    main()
