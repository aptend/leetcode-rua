from leezy import Solution, solution

from collections import defaultdict

class Q930(Solution):
    @solution
    def numSubarraysWithSum(self, A, S):
        # 304ms 64.03%
        # almost same with 560
        table = defaultdict(int)
        table[0] = 1
        accum, ans = 0, 0
        for x in A:
            accum += x
            ans += table[accum - S]
            table[accum] += 1
        return ans
    
    @solution
    def num_subarray_sum(self, A, S):
        # 280ms 93.68%
        # the sum of A won't exceed len(A)
        table = [0] * len(A)
        table[0] = 1
        accum, ans = 0, 0
        for x in A:
            accum += x
            ans += table[accum - S]
            table[accum] += 1
        return ans



def main():
    q = Q930()
    q.add_args([1, 0, 1, 0, 1], 2)
    q.run()


if __name__ == "__main__":
    main()
