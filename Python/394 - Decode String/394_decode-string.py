from leeyzer import Solution, solution


class Q394(Solution):
    @solution
    def decodeString(self, s):
        # 20ms 49.53%
        i = 0
        while i < len(s) and s[i].isalpha():
            i += 1
        if i == len(s): # pure string
            return s
        lead_str = s[:i]
        # s[i] is digit or [
        cnt = 0
        while s[i].isdigit():  # no boundry check when we have trusted input
            cnt = cnt * 10 + int(s[i])
            i += 1
        # now s[i] is '['
        open_ = 1
        j = i
        while j < len(s) and open_:
            j += 1
            if s[j] == '[':
                open_ += 1
            elif s[j] == ']':
                open_ -= 1
        return lead_str + cnt * self.decodeString(s[i+1:j]) + self.decodeString(s[j+1:])
    
    @solution
    def decode_str(self, s):
        pass


def main():
    q = Q394()
    q.add_args('3[a]2[bc]')
    q.add_args('3[a2[c]]')
    q.add_args('2[abc]3[cd]ef')
    q.run()


if __name__ == "__main__":
    main()
