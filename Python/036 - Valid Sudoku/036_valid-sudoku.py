from leezy import solution, Solution


class Q036(Solution):
    @solution
    def isValidSudoku(self, board):
        # 96ms 95.29%
        seen = set()
        for i, row in enumerate(board):
            for j, chess in enumerate(row):
                if chess == '.':
                    continue
                status = [(i, chess), (chess, j), (i//3, chess, j//3)]
                if any([x in seen for x in status]):
                    return False
                seen.update(status)
        return True


def main():
    q = Q036()
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    q.add_case(q.case(board).assert_equal(True))
    board[0][0] = '8'
    q.add_case(q.case(board).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
