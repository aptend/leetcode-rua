from leeyzer import solution, Solution

class Q1253(Solution):
    @solution
    def reconstructMatrix(self, upper, lower, colsum):
        # 760ms 100.00%
        A = [0] * len(colsum)
        B = [0] * len(colsum)
        ones = []
        for i, x in enumerate(colsum):
            if x == 2:
                A[i] = B[i] = 1
                upper -= 1
                lower -= 1
            elif x == 1:
                ones.append(i)
        if upper < 0 or lower < 0 or upper + lower != len(ones):
            return []
        for i in ones[:upper]:
            A[i] = 1
        for i in ones[upper:]:
            B[i] = 1
        return [A, B]


def main():
    q = Q1253()
    q.add_args(2, 1, [1, 1, 1])
    q.run()

if __name__ == '__main__':
    main()
