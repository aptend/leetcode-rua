from leezy import solution, Solution


class Q1094(Solution):
    @solution
    def carPooling(self, trips, capacity):
        # 60ms 92.68%
        cap = 0
        events = []
        for t in trips:
            # get off
            events.append((t[2], 0, t[0]))
            # get on
            events.append((t[1], 1, t[0]))
        for _, typ, person_cnt in sorted(events):
            if typ == 0:
                cap -= person_cnt
            else:
                cap += person_cnt
                if cap > capacity:
                    return False
        return True


def main():
    q = Q1094()
    q.add_case(q.case([[2, 1, 5], [3, 3, 7]], 4).assert_equal(False))
    q.add_case(q.case([[2, 1, 5], [3, 3, 7]], 5).assert_equal(True))
    q.add_case(q.case([[2, 1, 5], [3, 5, 7]], 3).assert_equal(True))
    q.add_case(q.case([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11).assert_equal(True))
    q.run()


if __name__ == '__main__':
    main()
