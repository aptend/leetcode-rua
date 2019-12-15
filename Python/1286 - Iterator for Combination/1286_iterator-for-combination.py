
class CombinationIterator:
    # 64ms 
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = combinationLength
        self.next_item = None
        self.iter = self.dfs(0, '')

    def dfs(self, s, acc):
        if len(acc) == self.length:
            yield acc
            return
        for i in range(s, len(self.chars)):
            yield from self.dfs(i + 1, acc+self.chars[i])

    def next(self) -> str:
        if self.next_item:
            r = self.next_item
            self.next_item = None
            return r
        else:
            return next(self.iter)

    def hasNext(self) -> bool:
        if self.next_item:
            return True
        try:
            self.next_item = next(self.iter)
        except StopIteration:
            return False
        else:
            return True


def main():
    combinationiterator = CombinationIterator('abc', 2)
    operations = ['next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext']
    oprands = [[], [], [], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(combinationiterator, opt):
            print(getattr(combinationiterator, opt).__call__(*opd))


if __name__ == '__main__':
    main()
