from leezy import Solution, solution


class Q991(Solution):
    @solution
    def brokenCalc(self, X, Y):
        if X >= Y:
            return X - Y
        else:
            return 1 + self.brokenCalc(X, Y // 2 if Y % 2 == 0 else Y + 1)

def main():
    q = Q991()
    q.add_args(2, 3)
    q.run()


if __name__ == "__main__":
    main()
