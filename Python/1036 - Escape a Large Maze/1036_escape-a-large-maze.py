from leezy import solution, Solution
from collections import deque


class Q1036(Solution):
    @solution
    def isEscapePossible(self, blocked, source, target):
        # 1316ms 23.53%
        blocks = set(tuple(item) for item in blocked)
        xs = [1, 0, -1, 0]
        ys = [0, 1, 0, -1]
        target = tuple(target)

        def bfs(source, target):
            cnt = 0
            q = deque()
            q.append(source)
            seen = set()
            while q and cnt < len(blocks):
                cnt += 1
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for di, dj in zip(xs, ys):
                        ni, nj = i + di, j + dj
                        npos = (ni, nj)
                        if npos == tuple(target):
                            return True
                        if not (0 <= ni < 10**6 and 0 <= nj < 10**6):
                            continue
                        if npos in blocks or npos in seen:
                            continue
                        seen.add(npos)
                        q.append(npos)
            return len(q) > 0
        return bfs(source, target) and bfs(target, source)

    @solution
    def escape(self, blocked, source, target):
        # 264ms 92.16%
        blocked = set(map(tuple, blocked))
        area = len(blocked) * (len(blocked) - 1) // 2
        source = tuple(source)
        target = tuple(target)

        def dfs(pos, target, seen):
            x, y = pos
            if not (0 <= x < 10**6 and 0 <= y < 10**6):
                return False
            if pos in blocked or pos in seen:
                return False
            seen.add(pos)
            if len(seen) > area or pos == target:
                return True
            return dfs((x + 1, y), target, seen) or dfs((x - 1, y), target, seen) or \
                dfs((x, y - 1), target, seen) or dfs((x, y + 1), target, seen)
        return dfs(source, target, set()) and dfs(target, source, set())


def main():
    q = Q1036()
    q.add_case(q.case([[0, 1], [1, 0]], [0, 0], [0, 2]).assert_equal(False))
    q.add_case(q.case([], [0, 0], [999999, 999999]).assert_equal(True))
    q.run()


if __name__ == '__main__':
    main()
