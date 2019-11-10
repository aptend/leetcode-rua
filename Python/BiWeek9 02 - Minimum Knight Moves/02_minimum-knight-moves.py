from leezy import Solution, solution

from collections import deque
class Q02(Solution):
    @solution
    def minKnightMoves(self, x, y):
        # 480ms 66.67%
        if x == 0 and y == 0:
            return 0
        dirs = [
            (1, 2), (1, -2), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (-2, 1), (-2, -1)
        ]
        q = deque()
        q.append((0, 0))
        # we just need to check a quarter of the whole chess board
        x, y = abs(x), abs(y)
        terminal = (x, y)
        seen = set()
        cnt = 0
        while q:
            cnt += 1
            for _ in range(len(q)):
                cx, cy = q.popleft()
                for di, dj in dirs:
                    nx, ny = cx + di, cy + dj
                    np = (nx, ny)
                    if np == terminal:
                        return cnt
                    # if x, y is accessable, we know that all path points are within 
                    # the rectangle [0, 0, x+2, y+2]
                    if np not in seen and 0 <= nx < x + 2 and 0 <= ny < y + 2:
                        seen.add(np)
                        q.append(np)
        return -1


def main():
    q = Q02()
    q.add_args(0, 0)
    q.add_args(2, 1)
    q.add_args(5, 5)
    q.add_args(11, 248) # 125
    q.run()


if __name__ == "__main__":
    main()
