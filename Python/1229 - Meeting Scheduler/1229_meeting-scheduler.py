from leeyzer import solution, Solution

class Q1229(Solution):
    @solution
    def minAvailableDuration(self, slots1, slots2, duration):
        # 532ms
        s1 = sorted([t for t in slots1 if t[1]-t[0] >= duration], key=lambda x: x[0])
        s2 = sorted([t for t in slots2 if t[1]-t[0] >= duration], key=lambda x: x[0])
        i = j = 0
        while i < len(s1) and j < len(s2):
            x1, y1 = s1[i]
            x2, y2 = s2[j]
            if min(y1, y2) - max(x1, x2) >= duration:
                return [max(x1, x2), max(x1, x2) + duration]
            # above 2 lines can replaced by following blabla
            # if x1 > y2:
            #     j += 1
            # elif x2 > y1:
            #     i += 1
            # elif x2 <= x1 and y1 <= y2:
            #     return [x1, x1 + duration]
            # elif x1 <= x2 and y2 <= y1:
            #     return [x2, x2 + duration]
            # elif x1 <= x2 and y1 - x2 >= duration:
            #     return [x2, x2 + duration]
            # elif x2 <= x1 and y2 - x1 >= duration:
            #     return [x1, x1 + duration]
            elif x1 < x2:
                i +=1
            else:
                j += 1
        return []


def main():
    q = Q1229()
    q.add_args([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
    q.run()

if __name__ == '__main__':
    main()
