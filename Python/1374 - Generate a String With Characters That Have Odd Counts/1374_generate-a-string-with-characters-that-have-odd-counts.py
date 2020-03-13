from leezy import solution, Solution


class Q1374(Solution):
    @solution
    def generateTheString(self, n):
        if n % 2 == 0:
            return 'a' * (n-1) + 'b'
        elif n > 1:
            return 'a' * (n-2) + 'b' + 'c'
        else:
            return 'a'


def main():
    q = Q1374()
    q.add_case(q.case(4))
    q.add_case(q.case(2))
    q.add_case(q.case(1))
    q.add_case(q.case(5))
    q.run()


if __name__ == '__main__':
    main()
