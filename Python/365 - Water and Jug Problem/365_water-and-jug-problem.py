from leezy import solution, Solution
from collections import deque


class Q365(Solution):
    @solution
    def canMeasureWater(self, x, y, z):
        #  3360ms 5.01%
        q = deque()
        q.append((0, 0))
        seen = {(0, 0)}
        while q:
            for _ in range(len(q)):
                j1, j2 = q.popleft()
                for c in [(0, j2),
                          (x, j2),
                          (0, j1+j2) if j1 <= (y-j2) else (j1+j2-y, y),
                          (j1, 0),
                          (j1, y),
                          (j1+j2, 0) if j2 <= (x-j1) else (x, j2+j1-x)]:
                    if sum(c) == z:
                        return True
                    if c not in seen:
                        seen.add(c)
                        q.append(c)
        return False

    @solution
    def jug_math(self, x, y, z):
        # 24 ms faster than 86.85%
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        if z == 0:
            return True
        if x == 0 or y == 0 or x + y < z:
            return False
        return z % gcd(x, y) == 0

    def jug_general_with_path(self, x, y, z):
        jugs = [x, y]
        target = z
        N = len(jugs)
        q = deque()
        init_stat = tuple(0 for _ in range(N))
        q.append(init_stat)
        seen = {init_stat}
        path = {init_stat: -1}
        while q:
            for _ in range(len(q)):
                stat = q.popleft()
                print(stat)
                for i in range(N):
                    candids = []
                    for j in range(N):
                        l = list(stat)
                        if i == j:
                            l[i] = 0
                            candids.append(tuple(l))
                            l[i] = jugs[i]
                            candids.append(tuple(l))
                        elif stat[i] <= jugs[j] - stat[j]:
                            l[i], l[j] = 0, stat[i]+stat[j]
                            candids.append(tuple(l))
                        else:
                            l[i], l[j] = stat[i]+stat[j]-jugs[j], jugs[j]
                            candids.append(tuple(l))
                    for c in candids:
                        if sum(c) == target:
                            ans = [c]
                            c = stat
                            while c != -1:
                                ans.append(c)
                                c = path[c]
                            ans.reverse()
                            return ans

                        if c not in seen:
                            seen.add(c)
                            path[c] = stat
                            q.append(c)
        return []


def main():
    q = Q365()
    q.add_case(q.case(3, 5, 4).assert_equal(True))
    q.add_case(q.case(0, 0, 0).assert_equal(True))
    q.add_case(q.case(2, 6, 5).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
