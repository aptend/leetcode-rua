from leezy import solution, Solution

class Q292(Solution):
    @solution
    def canWinNim(self, n):
        # idea about sub-problem
        return n % 4 != 0


def main():
    q = Q292()
    q.add_args(4)
    q.run()

if __name__ == '__main__':
    main()
