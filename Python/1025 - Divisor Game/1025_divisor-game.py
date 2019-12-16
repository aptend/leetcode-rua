from leezy import solution, Solution


class Q1025(Solution):
    @solution
    def divisorGame(self, N):
        return N % 2 == 0


def main():
    q = Q1025()
    q.add_case(q.case(2))
    q.run()


if __name__ == '__main__':
    main()
