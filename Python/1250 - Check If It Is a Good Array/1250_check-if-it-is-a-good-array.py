from leeyzer import solution, Solution

class Q1250(Solution):
    @solution
    def isGoodArray(self, nums):
        # 360ms
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = nums[0]
        for x in nums[1:]:
            g = gcd(g, x)
        return g == 1


def main():
    q = Q1250()
    q.add_args([12, 5, 7, 23])
    q.run()

if __name__ == '__main__':
    main()
