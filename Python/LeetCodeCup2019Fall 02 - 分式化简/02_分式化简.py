from leezy import Solution, solution


class Q02(Solution):
    @solution
    def fraction(self, cont):
        # 56ms
        def frac(conts):
            if len(conts) == 1:
                return [1, conts[0]]
            addin = conts[0]
            f = frac(conts[1:])
            f[0] += addin * f[1]
            f[0], f[1] = f[1], f[0]
            return f

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        ans = frac(cont)
        g = gcd(ans[0], ans[1])
        return [ans[1] // g, ans[0] // g]



def main():
    q = Q02()
    q.add_args([3, 2, 0, 2]) # [13, 5]
    q.add_args([0, 0, 3]) # [3, 1]
    q.run()


if __name__ == "__main__":
    main()
