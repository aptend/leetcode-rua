from leezy import solution, Solution


class Q1093(Solution):
    @solution
    def sampleStats(self, count):
        # 36ms 97.27%
        ans = [0.0] * 5
        for i, c in enumerate(count):
            if c > 0:
                ans[0] = float(i)
                break
        for i, c in enumerate(count[::-1]):
            if c > 0:
                ans[1] = float(255 - i)
                break
        N = sum(count)
        ans[2] = sum(i * c for i, c in enumerate(count)) / float(N)
        mid = 1 + (N - 1) // 2
        cnt = 0
        for i, c in enumerate(count):
            cnt += c
            if cnt > mid:
                ans[3] = float(i)
                break
            if cnt == mid:
                if N % 2 == 1:
                    ans[3] = float(i)
                else:
                    m = i
                    i += 1
                    while count[i] == 0:
                        i += 1
                    ans[3] = (m + i) / 2
                    break
        ans[4] = float(max((c, i) for i, c in enumerate(count))[1])
        return ans




def main():
    q = Q1093()
    q.add_case(q.case([0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    q.run()

if __name__ == '__main__':
    main()
