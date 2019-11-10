from leezy import Solution, solution


class Q844(Solution):
    @solution
    def backspaceCompare(self, S, T):
        # 8ms 99.44%
        def print_s(s):
            stack = []
            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            # str comp is somehow faster
            return ''.join(stack)
        return print_s(S) == print_s(T)
    
    @solution
    def backspace_compare(self, S, T):
        # 12ms 95.69%
        # every '#' only affects previous positions, so we think to handle from back
        i, j = len(S)-1, len(T)-1
        sback = tback = 0
        while True:
            # find the char that will REALLY be printed on the paper
            while i >= 0 and S[i] == '#':
                i -= 1
                sback += 1
                while i >= 0 and sback:
                    sback += 1 if S[i] == '#' else -1
                    i -= 1
            while j >= 0 and T[j] == '#':
                j -= 1
                tback += 1
                while j >= 0 and tback:
                    tback += 1 if T[j] == '#' else -1
                    j -= 1
            if i >= 0 and j >= 0:
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                else:
                    return False
            elif i < 0 and j < 0:
                return True
            else:
                return False


def main():
    q = Q844()
    q.add_args('ab#c', 'ad#c')
    q.add_args('ab##', 'c#d##')
    q.add_args('z#ab###c', 'ad#c')
    q.add_args('z####c##', 'ad#c')
    q.run()


if __name__ == "__main__":
    main()
