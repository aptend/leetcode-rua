from leeyzer import Solution, solution


class Q037(Solution):
    @solution
    def solveSudoku(self, board):
        # 132ms 78.27%
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        to_fill = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    rows[i].add(num)
                    columns[j].add(num)
                    blocks[i // 3][j // 3].add(num)
                else:
                    to_fill.append((i, j))

        def dfs(idx):
            if idx == len(to_fill):
                return True
            i, j = to_fill[idx]
            for guess in '123456789':
                bi, bj = i // 3, j // 3
                if (guess in rows[i] or
                        guess in columns[j] or
                        guess in blocks[bi][bj]):
                    continue
                rows[i].add(guess)
                columns[j].add(guess)
                blocks[bi][bj].add(guess)
                board[i][j] = guess
                if dfs(idx+1):
                    return True
                blocks[bi][bj].remove(guess)
                columns[j].remove(guess)
                rows[i].remove(guess)
                board[i][j] = '.'
            return False

        dfs(0)
        return board


def main():
    q = Q037()
    q.add_args([
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']])
    q.run()


if __name__ == "__main__":
    main()
