from leeyzer import solution, Solution

class Q1247(Solution):
    @solution
    def minimumSwap(self, s1, s2):
        # 40ms 50%
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == 'x':
                xy += 1
            else:
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        if xy % 2 == 0:
            return (xy + yx) // 2
        else:
            return xy // 2 + yx // 2 + 2


def main():
    q = Q1247()
    q.add_args('xx', 'yy')
    q.run()

if __name__ == '__main__':
    main()
