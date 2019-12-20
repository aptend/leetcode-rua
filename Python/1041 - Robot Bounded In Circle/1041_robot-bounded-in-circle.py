from leezy import solution, Solution


class Q1041(Solution):
    @solution
    def isRobotBounded(self, instructions):
        # 28ms 89.40%
        face = [0, 1]  # north
        pos = [0, 0]
        for ins in instructions:
            if ins == 'L':
                face[0], face[1] = -face[1], face[0]
            elif ins == 'R':
                face[0], face[1] = face[1], -face[0]
            else:
                pos[0] += face[0]
                pos[1] += face[1]
        return not (face == [0, 1] and pos != [0, 0])


def main():
    q = Q1041()
    q.add_case(q.case('GGLLGG').assert_equal(True))
    q.add_case(q.case('GG').assert_equal(False))
    q.add_case(q.case('GL').assert_equal(True))
    q.add_case(q.case('GLRLLGLL').assert_equal(True))

    q.run()

if __name__ == '__main__':
    main()
