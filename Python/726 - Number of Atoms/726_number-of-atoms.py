from leezy import Solution, solution
from collections import Counter
import re

class Q726(Solution):
    @solution
    def countOfAtoms(self, formula):
        # 12ms 99.18% 24ms 41.53%
        # O(n^2) actually, when input is like (((((..)))))
        def atom_counter(s):
            c = Counter()
            i = 0
            element = ''
            n = 0
            while i < len(s):
                ch = s[i]
                if ch.isupper():
                    if element:
                        c[element] += n if n else 1
                        n = 0
                    element = ch
                elif ch.islower():
                    element += ch
                elif ch.isdigit():
                    n = n*10 + int(ch)
                elif ch == '(':
                    open_ = 1
                    j = i
                    while open_:
                        j += 1
                        if s[j] == '(':
                            open_ += 1
                        if s[j] == ')':
                            open_ -= 1
                    factor = 0
                    k = j+1
                    while k < len(s) and s[k].isdigit():
                        factor = factor*10 + int(s[k])
                        k += 1
                    factor = factor if factor else 1
                    inner_c = atom_counter(s[i+1:j])
                    for key in inner_c:
                        inner_c[key] *= factor 
                    c += inner_c
                    i = k-1
                i += 1
            if element:
                c[element] += n if n else 1
            return c
        counter = atom_counter(formula)
        ans = ''
        for k in sorted(counter):
            if counter[k] > 1:
                ans += k + str(counter[k])
            else:
                ans += k
        return ans

class AtomConuter:

    def peek(self):
        return self.tokens[self.i]

    def next(self):
        ret = self.tokens[self.i]
        self.i += 1
        return ret

    def consume(self):
        self.i += 1

    def countOfAtoms(self, formula: str) -> str:
        self.tokens = re.findall(r'[A-Z][a-z]?|[()]|\d+', formula)
        self.tokens.append(None)
        self.i = 0
        counter = self.atom_block()
        ans = []

        for k in sorted(counter):
            ans.append(k)
            if (n := counter[k]) > 1:
                ans.append(str(n))
        return ''.join(ans)

    def atom_block(self):
        counter = Counter()
        while tk := self.next():
            if tk == ')':
                return counter
            elif tk == '(':
                inner_counter = self.atom_block()
                peeked = self.peek()
                if peeked and peeked.isdigit():
                    factor = int(peeked)
                    self.consume()
                    for k in inner_counter:
                        inner_counter[k] *= factor
                counter += inner_counter
            elif tk.isalpha():
                factor = 1
                peeked = self.peek()
                if peeked and peeked.isdigit():
                    factor = int(peeked)
                    self.consume()
                counter[tk] += factor

        return counter

def main():
    q = Q726()
    q.add_args('H2O')
    q.add_args('(BN3)33')
    q.add_args('Mg(OH)2')
    q.add_args('((HHe28Be26He)9)34')
    q.add_args('K4(ON(SO3)2)2')
    q.run()


if __name__ == "__main__":
    main()
