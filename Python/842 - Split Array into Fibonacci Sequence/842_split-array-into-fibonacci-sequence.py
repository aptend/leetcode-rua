from leezy import Solution, solution
import sys

class Q842(Solution):
    @solution
    def splitIntoFibonacci(self, S):
        # 24ms 84.92%
        current = []
        self.dfs(S, 0, current)
        return current

    def dfs(self, S, start, current):
        if start == len(S):
            return len(current) > 2 
        k = len(current)
        val = float('inf')
        if k >= 2:
            val = current[-1]+current[-2]
        option = 0
        # 2^31 has 10 digits
        for i in range(start, min(len(S), start+10)):
            if i > start and S[start] == '0':
                break
            option = option*10 + int(S[i])
            if option > (1 << 31) or option > val:
                break
            if k <= 1 or option == val:
                current.append(option)
                if self.dfs(S, i+1, current):
                    return current
                current.pop()
        return False


def main():
    q = Q842()
    q.add_args('17522')
    q.add_args('123456579')
    q.add_args('11235813')
    q.add_args('0123')
    q.add_args('1101111')
    q.add_args('539834657215398346785398346991079669377'
               '16195040762699173453431867752'
               '9701785098211336528511')
    q.run()


if __name__ == "__main__":
    main()
