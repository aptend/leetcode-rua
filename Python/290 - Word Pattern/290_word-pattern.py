from leeyzer import Solution, solution


class Q290(Solution):
    @solution
    def wordPattern(self, pattern, str):
        pass


def main():
    q = Q290()
    q.add_args('abba', 'dog cat cat dog')
    q.run()


if __name__ == "__main__":
    main()
