from leezy import solution, Solution


class Q1024(Solution):
    @solution
    def videoStitching(self, clips, T):
        # 24ms 98.70%
        if not clips:
            return -1
        clips = sorted(clips, key=lambda x: (x[0], x[0]-x[1]))
        if clips[0][0] > 0:
            return -1
        if clips[0][1] >= T:
            return 1
        stack = [clips[0]]
        for c in clips[1:]:
            if c[1] > stack[-1][1]:
                cnt = 1
                while cnt <= len(stack) and stack[-cnt][1] >= c[0]:
                    cnt += 1
                if cnt == 1:
                    return -1
                for _ in range(cnt-2):
                    stack.pop()
                stack.append(c)
            if stack[-1][1] >= T:
                return len(stack)
        return -1



def main():
    q = Q1024()
    q.add_case(q.case([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    q.add_case(q.case([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [
               1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9))
    q.add_case(q.case([[0, 4], [2, 8]], 5))
    q.run()

if __name__ == '__main__':
    main()
