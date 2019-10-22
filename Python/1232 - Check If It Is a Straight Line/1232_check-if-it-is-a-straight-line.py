from leeyzer import solution, Solution

class Q1232(Solution):
    @solution
    def checkStraightLine(self, coordinates):
        # 72ms 76.51%
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2:
            return all(p[0] == x1 for p in coordinates)
        else:
            for x, y in coordinates[2:]:
                if not (x-x1)*(y2-y1) == (y-y1)*(x2-x1):
                    return False
            return True


def main():
    q = Q1232()
    q.add_args([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    q.run()

if __name__ == '__main__':
    main()
