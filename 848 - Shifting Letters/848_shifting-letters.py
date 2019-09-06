from leeyzer import Solution, solution


class Q848(Solution):
    @solution
    def shiftingLetters(self, S, shifts):
        # 172ms 70.12%
        N = len(shifts)
        shifts.append(0)
        for i in range(N-1, -1, -1):
            # refer to Karp-Robin
            shifts[i] = (shifts[i] % 26 + shifts[i+1]) % 26
        A = list('abcdefghijklmnopqrstuvwxyz')
        BASE = ord('a')
        ans = []
        for i, ch in enumerate(S):
            idx = (ord(ch) - BASE + shifts[i]) % 26
            ans.append(A[idx])
        return ''.join(ans)
    


def main():
    q = Q848()
    q.add_args('abc', [3, 5, 9])
    q.run()


if __name__ == "__main__":
    main()
