from leezy import Solution, solution
from collections import deque

class Q1184(Solution):
    @solution
    def distanceBetweenBusStops(self, distance, start, destination):
        # 52ms 89.08%
        a, b = min(start, destination), max(start, destination)
        queue = deque(distance)
        queue.rotate(-a)
        right_dist = left_dist = 0
        for i in range(b-a):
            right_dist += queue[i]
        for i in range(b-a, len(distance)):
            left_dist += queue[i]
        return min(left_dist, right_dist)

    @solution
    def distance_between_busstops(self, distance, start, destination):
        # 52ms
        a, b = min(start, destination), max(start, destination)
        right_dist = sum(distance[a:b])
        left_dist = sum(distance[:a]) + sum(distance[b:])
        return min(left_dist, right_dist)


def main():
    q = Q1184()
    q.add_args([1, 2, 3, 4], 2, 0)
    q.add_args([1, 2, 3, 4], 0, 2)
    q.add_args([1, 2, 3, 4], 0, 3)
    q.run()


if __name__ == "__main__":
    main()
