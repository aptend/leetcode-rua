from leezy import solution, Solution


class Q071(Solution):
    @solution
    def simplifyPath(self, path):
        # 32ms 60.67%
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
    
    @solution
    def simplify_without_split(self, path):
        # 24ms
        stack = []
        formed = ''
        for ch in path+'/':
            if ch == '/':
                if not formed or formed == '.':
                    pass
                elif formed == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(formed)
                formed = ''
            else:
                formed += ch
        return '/' + '/'.join(stack)





def main():
    q = Q071()
    q.add_case(q.case('/home/').assert_equal('/home'))
    q.add_case(q.case('/home//foo/').assert_equal('/home/foo'))
    q.add_case(q.case('/../').assert_equal('/'))
    q.add_case(q.case('/a/./b/../../c/').assert_equal('/c'))
    q.add_case(q.case('/a/../../b/../c//.//').assert_equal('/c'))
    q.add_case(q.case('/a//b////c/d//././/..').assert_equal('/a/b/c'))
    q.add_case(q.case('/abc').assert_equal('/abc'))
    q.run()

if __name__ == '__main__':
    main()
