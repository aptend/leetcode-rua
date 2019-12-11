from leezy import solution, Solution

from heapq import heappop, heappush

class Q218(Solution):
    @solution
    def getSkyline(self, buildings):
        # 116ms 95.31%
        sky = [[-1, 0]]
        position = set()
        for l, r, _ in buildings:
            position.add(l)
            position.add(r)

        # 被当前扫描线选中的大楼
        live = []
        i = 0
        for t in sorted(position):
            # 加入起点在扫描线左侧的大楼
            # 等号保证重叠的building也被加入
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            # 扫描线可能扫到了当前最高楼的结束边，就尝试pop
            # 保证了pop结束后，heap顶是剩下的最高的楼
            while live and live[0][1] <= t:
                heappop(live)

            # 考虑了开始事件和结束事件之后，尝试加入当前楼房的最高点
            # 之加入不同值的节点，避免错误添加
            h = -live[0][0] if live else 0
            if sky[-1][1] != h:
                sky.append([t, h])
        return sky[1:]


def main():
    q = Q218()
    q.add_case(
        q.case([[2, 9, 10],
                [3, 7, 15],
                [5, 12, 12],
                [15, 20, 10],
                [19, 24, 8]]))
    q.run()


if __name__ == '__main__':
    main()
