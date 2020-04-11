from leezy import solution, Solution


class Q151(Solution):

    @solution
    def reverseWords(self, s):
        # O(1) space
        s = list(s)

        # squeeze out extra gap between words
        i = 0
        prev = ''
        for ch in s:
            if ch != ' ':
                if prev == ' ' and i > 0:
                    s[i] = ' '
                    i += 1
                s[i] = ch
                i += 1
            prev = ch
        # pop trailing characters
        s = s[:i]

        def rev(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        # reverse the sentence
        rev(s, 0, len(s)-1)

        # reverse every word
        s.append(' ')
        i = 0
        for j in range(len(s)):
            if s[j] == ' ':
                rev(s, i, j-1)
                i = j + 1
        s.pop()
        return ''.join(s)


def main():
    q = Q151()
    q.add_case(q.case('the sky is blue').assert_equal('blue is sky the'))
    q.add_case(q.case('  hello world!  ').assert_equal('world! hello'))
    q.add_case(q.case('a good   example').assert_equal('example good a'))
    q.add_case(q.case('       ').assert_equal(''))
    q.add_case(q.case('').assert_equal(''))
    q.run()


if __name__ == '__main__':
    main()
