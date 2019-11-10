from leezy import Solution, solution


class Q830(Solution):
    @solution
    def largeGroupPositions(self, S):
        # 48ms 50.57%
        N = len(S)
        ans = []
        start = i = 0
        for i in range(N-1):
            if S[i] != S[i+1]:
                if i - start >= 2:
                    ans.append([start, i])
                start = i + 1
        if N - 1 - start >= 2:
            ans.append([start, N-1])
        return ans


def main():
    q = Q830()
    q.add_args('abbxxxxzzy')
    q.run()


if __name__ == "__main__":
    main()
