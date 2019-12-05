from leezy import solution, Solution

from collections import Counter

class Q347(Solution):
    @solution
    def topKFrequent(self, nums, k):
        # 96ms 99.34% O(n*logn)
        return [item[0] for item in Counter(nums).most_common(k)]
    
    @solution
    def top_k(self, nums, k):
        # 120ms 55.05% O(n)
        N = len(nums)
        count_map = [[] for _ in range(N+1)]
        for v, cnt in Counter(nums).items():
            count_map[cnt].append(v)
        
        ans = []
        for i in range(N, -1, -1):
            if len(ans) == k:
                return ans
            ans.extend(count_map[i])


def main():
    q = Q347()
    q.add_case(q.case([1, 1, 1, 2, 2, 3], 2))
    q.run()

if __name__ == '__main__':
    main()
