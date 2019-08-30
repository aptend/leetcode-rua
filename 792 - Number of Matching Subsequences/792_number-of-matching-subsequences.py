from leeyzer import Solution, solution

from collections import defaultdict
from bisect import bisect_left

class Q792(Solution):
    @solution
    def numMatchingSubseq(self, S, words):
        # 608ms 61.80%
        idx_map = defaultdict(list)
        for idx, ch in enumerate(S):
            idx_map[ch].append(idx)

        def is_subseq(s):
            # 372. is subsequence
            threshold = 0
            for ch in s:
                array = idx_map[ch]
                idx = bisect_left(array, threshold)
                if idx == len(array):
                    return False
                threshold = array[idx] + 1
            return True
        return sum(is_subseq(w) for w in words)

    @solution
    def num_match_subseq(self, S, words):
        # 444ms 84.49%
        pool = defaultdict(list)
        for w in words:
            pool[w[0]].append(w)
        ans = 0
        for ch in S:
            to_be_pumped = pool[ch]
            pool[ch] = []
            for w in to_be_pumped:
                if len(w) == 1:
                    ans += 1
                else:
                    pool[w[1]].append(w[1:])
        return ans



def main():
    q = Q792()
    q.add_args('abcde', ['a', 'bb', 'acd', 'ace'])
    q.run()


if __name__ == "__main__":
    main()
