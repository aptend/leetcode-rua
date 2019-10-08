from leeyzer import Solution, solution

from heapq import heappop, heappush
from collections import deque


class Q818(Solution):
    @solution
    def racecar(self, target):
        # 2012ms 25.49%
        heap = [(0, 0, 1)]
        turn_points = set()
        while heap:
            dist, pos, spd = heappop(heap)
            if pos == target:
                return dist
            if pos < 0:
                continue
            # forward
            heappush(heap, (dist+1, pos+spd, spd*2))
            r_stat = (pos, 1 if spd < 0 else -1)
            if r_stat not in turn_points:
                turn_points.add(r_stat)
                heappush(heap, (dist+1, pos, r_stat[1]))

    @solution
    def race_car(self, target):
        # 1536ms 28.74%
        if target == 0:
            return 0
        q = deque()
        q.append((0, 1))
        turn_points = set()
        turn_points.add((0, 1))
        turn_points.add((0, -1))
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                pos, v = q.popleft()
                if pos + v == target:
                    return step
                q.append((pos+v, v * 2))
                r_stat = (pos, 1 if v < 0 else -1)
                if r_stat not in turn_points:
                    turn_points.add(r_stat)
                    q.append(r_stat)


def main():
    q = Q818()
    q.add_args(3)
    q.add_args(6)
    q.add_args(0)
    q.add_args(330)

    q.run()


if __name__ == "__main__":
    main()
