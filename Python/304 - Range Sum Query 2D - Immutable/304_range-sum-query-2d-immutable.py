from pprint import pprint

class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # 80ms 99.64% / 108ms
        m, n = len(matrix), len(matrix[0])
        accum_m = [[0]*(n+1)]
        for i in range(1, m+1):
            acc = [0]
            for j in range(1, n+1):
                acc.append(acc[j-1] + matrix[i-1][j-1] +
                           accum_m[i-1][j] - accum_m[i-1][j-1])
            accum_m.append(acc)
        self.accum_m = accum_m

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        whole_m = self.accum_m[row2+1][col2+1]
        left_m = self.accum_m[row2+1][col1]
        top_m = self.accum_m[row1][col2+1]
        left_top_m = self.accum_m[row1][col1]
        return whole_m + left_top_m - left_m - top_m


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
def main():
    nummatrix = NumMatrix([[3, 0, 1, 4, 2],
                           [5, 6, 3, 2, 1],
                           [1, 2, 0, 1, 5],
                           [4, 1, 0, 1, 7],
                           [1, 0, 3, 0, 5]])
    operations = ['sumRegion', 'sumRegion', 'sumRegion']
    operands = [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    for opt, opd in zip(operations, operands):
        if hasattr(nummatrix, opt):
            print(getattr(nummatrix, opt).__call__(*opd))


if __name__ == "__main__":
    main()
