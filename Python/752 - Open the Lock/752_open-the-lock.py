from leeyzer import Solution, solution
from collections import deque

class Q752(Solution):
    @solution
    def openLock(self, deadends, target):
        # 316ms 87.75%
        deadends = set(int(dd) for dd in deadends)
        if 0 in deadends:
            return -1
        power = [1, 10, 100, 1000]
        target = int(target)
        queue = deque()
        queue.append(0)
        seen = set()
        cnt = -1
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                src = queue.popleft()
                for i in range(4):
                    x = (src // power[i]) % 10
                    for flag in (1, -1):
                        delta = ((x + flag) % 10 - x) * power[i]
                        nxt = src + delta
                        if nxt == target:
                            return cnt + 1
                        if nxt in deadends or nxt in seen:
                            continue
                        seen.add(nxt)
                        queue.append(nxt)
        return -1
    
    @solution
    def openLock_bidfs(self, deadends, target):
        # 76ms 99.84%
        deadends = set(int(dd) for dd in deadends)
        if 0 in deadends:
            return -1
        power = [1, 10, 100, 1000]
        target = int(target)
        s1, s2, seen = {0}, {target}, set()
        cnt = -1
        while s1 and s2:
            cnt += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            nxt_s = set()
            for src in s1:
                for i in range(4):
                    x = (src // power[i]) % 10
                    for flag in (1, -1):
                        delta = ((x + flag) % 10 - x) * power[i]
                        nxt = src + delta
                        if nxt in s2:
                            return cnt + 1
                        if nxt in deadends or nxt in seen:
                            continue
                        nxt_s.add(nxt)
            s1 = nxt_s
        return -1



def main():
    q = Q752()
    q.add_args(['0201', '0101', '0102', '1212', '2002'], '0202')
    q.add_args(['8888'], '0009')
    q.add_args(['0000'], '8888')
    q.run()


if __name__ == "__main__":
    main()
