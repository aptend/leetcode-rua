from leezy import solution, Solution

from random import randint

def rand7():
    return randint(1, 7)

class Q470(Solution):
    @solution
    def call_rand10(self, n):
        return [self.rand10() for _ in range(n)]

    def rand10(self):
        random40 = float('inf')
        while random40 >= 40:
            random40 = (rand7() - 1) * 7 + rand7() - 1
        return random40 % 10 + 1


def main():
    q = Q470()
    q.add_case(q.case(5))
    q.run()

if __name__ == '__main__':
    main()
