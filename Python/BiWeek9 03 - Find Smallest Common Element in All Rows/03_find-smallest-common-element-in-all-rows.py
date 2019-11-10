from leezy import Solution, solution

from bisect import bisect_left
class Q02(Solution):
    @solution
    def smallestCommonElement(self, mat):
        for x in mat[0]:
            for row in mat[1:]:
                idx = bisect_left(row, x)
                if idx == len(row) or row[idx] != x:
                    break
            else:
                return x
        return -1



def main():
    q = Q02()
    q.add_args([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10],
                [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]])
    q.run()


if __name__ == "__main__":
    main()
