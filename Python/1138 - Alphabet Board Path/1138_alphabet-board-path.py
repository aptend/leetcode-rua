from leezy import Solution, solution


class Q1138(Solution):
    @solution
    def alphabetBoardPath(self, target):
        # 12ms 94.74%
        ans = []
        base = ord('a')
        t = 'a' + target
        for src, dst in zip(t, t[1:]):
            ns = ord(src) - base
            nd = ord(dst) - base
            x1, y1 = divmod(ns, 5)
            x2, y2 = divmod(nd, 5)
            if src == 'z':
                ans += ['D' if x2 > x1 else 'U'] * abs(x1-x2)
                ans += ['R' if y2 > y1 else 'L'] * abs(y1-y2)
            else:
                ans += ['R' if y2 > y1 else 'L'] * abs(y1-y2)
                ans += ['D' if x2 > x1 else 'U'] * abs(x1-x2)
            ans.append('!')
        return ''.join(ans)


def main():
    q = Q1138()
    q.add_args('leet')
    q.run()


if __name__ == "__main__":
    main()
