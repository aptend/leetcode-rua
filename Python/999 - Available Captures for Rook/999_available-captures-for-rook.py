from leezy import solution, Solution


class Q999(Solution):
    @solution
    def numRookCaptures(self, board):
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])
        ans = 0
        handled = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    handled = True
                    for k in range(i+1, m):
                        if board[k][j] == 'B':
                            break
                        if board[k][j] == 'p':
                            ans += 1
                            break
                    for k in range(i-1, -1, -1):
                        if board[k][j] == 'B':
                            break
                        if board[k][j] == 'p':
                            ans += 1
                            break
                    for k in range(j+1, n):
                        if board[i][k] == 'B':
                            break
                        if board[i][k] == 'p':
                            ans += 1
                            break
                    for k in range(j-1, -1, -1):
                        if board[i][k] == 'B':
                            break
                        if board[i][k] == 'p':
                            ans += 1
                            break
            if handled:
                break
        return ans


def main():
    q = Q999()
    q.add_case(q.case([
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'p', '.', '.', '.', '.'],
        ['.', '.', '.', 'R', '.', '.', '.', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'p', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
