from leeyzer import solution, Solution

class Q231(Solution):
    @solution
    def isPowerOfTwo(self, n):
        return n != 0 and n & (n - 1) == 0


def main():
    q = Q231()
    q.add_args(1)
    q.run()

if __name__ == '__main__':
    main()
