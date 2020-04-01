from leezy import Solution, solution
from collections import defaultdict
from functools import reduce


class Q820(Solution):
    @solution
    def minimumLengthEncoding(self, words):
        ans = 0
        pool = set()
        for w in sorted(words, key=lambda w: -len(w)):
            if w not in pool:
                n = len(w)
                ans += n + 1
                for i in range(n-1):
                    pool.add(w[i:])
        return ans

    @solution
    def min_len_initial(self, words):
        # 140ms 70.24%
        w_set = set(words)
        words = sorted(w_set, key=lambda x: x[::-1])
        N = len(words)
        for i in range(N-1):
            # after sorted, if words[i] can be contained by another,
            # it must be words[i+1]
            if words[i+1].endswith(words[i]):
                w_set.remove(words[i])
        cnt = 0
        for w in w_set:
            cnt += len(w) + 1
        return cnt

    @solution
    def min_len_encoding(self, words):
        # 136ms
        w_set = set(words)
        for w in list(w_set):
            for i in range(1, len(w)):
                w_set.discard(w[i:])
        cnt = 0
        for w in w_set:
            cnt += len(w) + 1
        return cnt

    @solution
    def min_len_encoding_trie(self, words):
        # 192ms
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        def Trie(): return defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


def main():
    q = Q820()
    q.add_case(q.case(['time', 'me', 'bell']).assert_equal(10))
    q.add_case(q.case(['time', 'xme', 'bell']).assert_equal(14))
    q.run()


if __name__ == "__main__":
    main()
