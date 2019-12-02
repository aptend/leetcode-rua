from leezy import solution, Solution


class Q289(Solution):
    @solution
    def gameOfLife(self, board):
        # 32ms 89.76%
        """
        0: 0x00  dead -> dead
        1: 0x01  live -> dead
        2: 0x10  dead -> live
        3: 0x11  live -> live
        """
        if not board:
            return
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for nb in neighbors:
                    x, y = i+nb[0], j+nb[1]
                    if -1 < x < m and -1 < y < n:
                        count += board[x][y] & 0x1
                if board[i][j] & 0x01 == 0:
                    if count == 3:
                        board[i][j] = 2  # dead -> live
                    # else: = 0          # dead -> dead
                else:
                    if 2 <= count <= 3:
                        board[i][j] = 3  # live -> live
                    # else: = 1          # live -> dead

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        return board



def main():
    q = Q289()
    q.add_case(q.case([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    q.run()

if __name__ == '__main__':
    main()
