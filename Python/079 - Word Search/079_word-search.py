from leezy import Solution, solution


class Q079(Solution):
    @solution
    def exist(self, board, word):
        if word == '':
            return True
        if not board:
            return False
        if not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word, board, i, j):
                    return True
        return False

    def dfs(self, suffix, board, x, y):
        if suffix == '':
            return True
        if (x < 0 or x >= len(board) or
                y < 0 or y >= len(board[0]) or
                board[x][y] != suffix[0]):
            return False
        tmp = board[x][y]
        board[x][y] = '#'
        nxt_suffix = suffix[1:]
        found = (self.dfs(nxt_suffix, board, x+1, y) or
                 self.dfs(nxt_suffix, board, x-1, y) or
                 self.dfs(nxt_suffix, board, x, y+1) or
                 self.dfs(nxt_suffix, board, x, y-1))
        board[x][y] = tmp
        return found


def main():
    q = Q079()
    q.add_args([['a', 'a']], 'aaa')    
    q.add_args([["a", "a", "a", "a"],
                ["a", "a", "a", "a"]], "aaaaaaaaa")
    q.add_args([["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]], "ABCCED")
    q.add_args([["A", "B", "C", "E"],
                ["S", "F", "E", "S"],
                ["A", "D", "E", "E"]], "ABCESEEEFS")
    q.run()


if __name__ == "__main__":
    main()
