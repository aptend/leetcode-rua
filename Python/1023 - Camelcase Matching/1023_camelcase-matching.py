from leezy import solution, Solution


class Q1023(Solution):
    @solution
    def camelMatch(self, queries, pattern):
        # 28ms 92.70%
        def match(s, p):
            j = 0
            for ch in s:
                if ch.isupper():
                    if j < len(p) and p[j] == ch:
                        j += 1
                    else:
                        return False
                else:
                    if j < len(p) and p[j] == ch:
                        j += 1
            return j == len(p)
        return [match(q, pattern) for q in queries]


def main():
    q = Q1023()
    case0 = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    q.add_case(q.case(case0, 'FB').assert_equal([True, False, True, True, False]))
    q.add_case(q.case(case0, 'FoBa').assert_equal([True, False, True, False, False]))
    q.add_case(q.case(case0, 'FoBaT').assert_equal([False, True, False, False, False]))
    q.run()


if __name__ == '__main__':
    main()
