from leezy import solution, Solution

class Q338(Solution):
    @solution
    def countBits(self, num):
        # 88ms 97.53%
        # i base
        # 1   1
        # 2   2
        # 3   2
        # 4   4
        # 5   4
        # 6   4
        # 7   4
        # 8   8
        ans = [0] * (num + 1)
        base = 1
        threshold = 1
        for i in range(1, num+1): 
            if i == threshold:
                base = threshold
                threshold *= 2
            ans[i] = ans[i-base] + 1
        return ans


def main():
    q = Q338()
    q.add_args(2)
    q.add_args(5)
    q.run()

if __name__ == '__main__':
    main()
