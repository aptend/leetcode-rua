from leezy import solution, Solution

from collections import defaultdict

class Q049(Solution):
    @solution
    def groupAnagrams(self, strs):
        table = defaultdict(list)
        for s in strs:
            table[tuple(sorted(s))].append(s)
        return list(table.values())


def main():
    q = Q049()
    q.add_args(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    q.run()

if __name__ == '__main__':
    main()
