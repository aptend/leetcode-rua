from leezy import solution, Solution


class Q056(Solution):
    @solution
    def merge(self, intervals):
        # 76 ms, 98.92%
        if len(intervals) <= 1:
            return intervals
        s_intervals = sorted(intervals, key=lambda v: v[0])
        cur_v = s_intervals[0]
        ans = []
        for v in s_intervals[1:]:
            if v[0] > cur_v[1]:
                ans.append(cur_v)
                cur_v = v
            else:
                cur_v[1] = max(cur_v[1], v[1])
        ans.append(cur_v)
        return ans



def main():
    q = Q056()
    q.add_case(q.case([[1, 3], [2, 6], [8, 10], [15, 18]]))
    q.add_case(q.case([[1, 4], [4, 5]]))
    q.run()

if __name__ == '__main__':
    main()
