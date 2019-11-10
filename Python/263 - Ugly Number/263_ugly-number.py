from leezy import Solution, solution


class Q263(Solution):
    @solution
    def isUgly(self, num):
        # 40ms
        prev = num
        while True:
            for f in (2, 3, 5):
                if num % f == 0:
                    num //= f
            if prev == num:
                break
            prev = num
        return num == 1
    
    @solution
    def is_ugly(self, num):
        # 36ms 83.25%
        if num == 0:
            return False
        for f in (2, 3, 5):
            while num % f == 0:
                num //= f
        return num == 1



def main():
    q = Q263()
    q.add_args(0)
    q.add_args(6)
    q.add_args(7)
    q.add_args(12)
    q.run()


if __name__ == "__main__":
    main()
