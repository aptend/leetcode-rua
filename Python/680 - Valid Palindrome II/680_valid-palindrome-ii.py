from leeyzer import Solution, solution


class Q680(Solution):
    @solution
    def validPalindrome(self, s):
        # 140ms 53.58%
        def is_valid(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return is_valid(i+1, j) or is_valid(i, j-1)
            i += 1
            j -= 1
        return True
    
    @solution
    def valid_palindrome(self, s):
        # 76ms 88.37%
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]:
                p1, p2 = s[i+1:j+1], s[i:j]
                return p1 == p2[::-1] or p2 == p2[::-1]
            i += 1
            j -= 1
        return True


def main():
    q = Q680()
    q.add_args('aba')
    q.run()


if __name__ == "__main__":
    main()
