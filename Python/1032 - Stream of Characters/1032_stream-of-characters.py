
class StreamChecker:
    # 1304ms 49.00%
    def __init__(self, words):
        """
        :type words: List[str]
        """
        suff_words = {}
        for w in words:
            n = len(w)
            for i in range(n-1):
                tmp_w = w[n-i-1:]
                if tmp_w not in suff_words:
                    suff_words[tmp_w] = False
            suff_words[w] = True
        self.words = suff_words

        self.len = max(len(w) for w in words)
        self.queries = ''

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.queries += letter
        N = len(self.queries)
        for i in range(N):
            q = self.queries[N-i-1:]
            if q not in self.words:
                break
            elif self.words[q]:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

def main():
    streamchecker = StreamChecker(['cd', 'f', 'kl'])
    operations = ['query', 'query', 'query', 'query', 'query', 'query', 'query', 'query', 'query', 'query', 'query', 'query']
    oprands = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l']]
    for opt, opd in zip(operations, oprands):
        if hasattr(streamchecker, opt):
            print(getattr(streamchecker, opt).__call__(*opd))


if __name__ == '__main__':
    main()
