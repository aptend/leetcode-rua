from leezy import Solution, solution

from collections import Counter, defaultdict
class Q869(Solution):
    @solution
    def reorderedPowerOf2(self, N):
        # 44ms
        x = 1
        table = defaultdict(list)
        while x < 10 ** 9:
            x_str = str(x)
            n_digits = len(x_str)
            table[n_digits].append(Counter(x_str))
            x <<= 1
        n_str = str(N)
        return Counter(n_str) in table[len(n_str)]

    @solution
    def reordered_power(self, N):
        # 32ms 99.03%
        c = Counter(str(N))
        return any(c == Counter(str(1 << x)) for x in range(30))




def main():
    q = Q869()
    q.add_args(1)
    q.add_args(153454323)
    q.run()


if __name__ == "__main__":
    main()
