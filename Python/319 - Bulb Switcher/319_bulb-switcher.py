from leezy import solution, Solution


# interesting math problem
# reverse thinking
import math
class Q319(Solution):
    @solution
    def bulbSwitch(self, n):
        return int(math.sqrt(n))


def main():
    q = Q319()
    q.add_case(q.case(3))
    q.run()

if __name__ == '__main__':
    main()
