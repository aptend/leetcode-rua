from leezy import solution, Solution


class Q306(Solution):
    @solution
    def isAdditiveNumber(self, num):
        # 28ms 86.26%
        N = len(num)
        for i in range(1, (N * 2) // 3):
            for j in range(1, i+1):
                a = num[:j]
                b = num[j:i+1]
                if j > 1 and a[0] == '0':
                    return False
                if j < i and b[0] == '0':
                    continue

                c = str(int(a) + int(b))
                leftover = num[i+1:]
                while leftover.startswith(c):
                    leftover = leftover[len(c):]
                    b, c = c, str(int(b) + int(c))
                if leftover == '':
                    return True
        return False


def main():
    q = Q306()
    q.add_case(q.case('112358'))
    q.run()

if __name__ == '__main__':
    main()
