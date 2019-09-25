from leeyzer import Solution, solution


class Q02(Solution):
    @solution
    def game(self, guess, answer):
        return sum([x == y for x, y in zip(guess, answer)])

def main():
    q = Q02()
    q.add_args([1, 2, 3], [1, 2, 3])
    q.add_args([2, 2, 3], [3, 2, 1])
    q.run()


if __name__ == "__main__":
    main()
