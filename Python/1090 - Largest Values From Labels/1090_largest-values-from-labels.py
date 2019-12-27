from leezy import solution, Solution
from collections import defaultdict


class Q1090(Solution):
    @solution
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        # 136ms 97.98%
        N = len(values)
        idxs = sorted(range(N), key=lambda x: values[x], reverse=True)
        label_cnt = defaultdict(int)
        ans = 0
        cnt = 0
        for i in idxs:
            if label_cnt[labels[i]] < use_limit:
                label_cnt[labels[i]] += 1
                ans += values[i]
                cnt += 1
                if cnt == num_wanted:
                    break
        return ans


def main():
    q = Q1090()
    q.add_case(q.case([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1).assert_equal(9))
    q.add_case(q.case([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1).assert_equal(16))
    
    q.run()


if __name__ == '__main__':
    main()
