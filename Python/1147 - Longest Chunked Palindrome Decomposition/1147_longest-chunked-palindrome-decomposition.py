from leezy import solution, Solution


class Q1147(Solution):
    @solution
    def longestDecomposition(self, text):
        ans = 0
        start = 0
        chars_n = len(text)

        while chars_n > 1:
            end = len(text) - start
            for k in range(1, 1 + chars_n // 2):
                if text[start: start+k] == text[end-k:end]:
                    ans += 2
                    start = start+k
                    chars_n -= k * 2
                    break
            else:
                # see it as a whole part
                chars_n = 1
        return ans + chars_n





def main():
    q = Q1147()
    q.add_case(q.case('ghiabcdefhelloadamhelloabcdefghi').assert_equal(7))
    q.add_case(q.case('merchant').assert_equal(1))
    q.add_case(q.case('antaprezatepzapreanta').assert_equal(11))
    q.add_case(q.case('aaa').assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
