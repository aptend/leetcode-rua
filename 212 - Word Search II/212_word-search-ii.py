from leeyzer import Solution, solution


class Q212(Solution):
    """
    292ms beats 92.04%
    用前缀字典代替trie
    jieba分词就是这么做的，效果还行
    """
    @solution
    def findWords(self, board, words):
        if not board:
            return []
        m, n = len(board), len(board[0])
        results = set()
        prefix_dict = {}
        for word in words:
            prefix_dict[word] = True
            for k in range(1, len(word)):
                w = word[:k]
                if w in prefix_dict and prefix_dict[w]:
                    continue
                prefix_dict[w] = False
        
        on_stack = set()
        def dfs(i, j, formed):
            formed += board[i][j]
            if formed not in prefix_dict or (i, j) in on_stack:
                return
            if prefix_dict[formed]:
                results.add(formed)

            on_stack.add((i, j))
            if i > 0:
                dfs(i-1, j, formed)
            if i < m-1:
                dfs(i+1, j, formed)
            if j > 0:
                dfs(i, j-1, formed)
            if j < n-1:
                dfs(i, j+1, formed)
            on_stack.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, '')
        return list(results)


def main():
    q = Q212()
    q.add_args([
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'a', 'r'],
        ['i', 'f', 'i', 'n']
    ],
        ['oath', 'pea', 'eat', 'rain', 'a', 'thth'])
    q.run()


if __name__ == "__main__":
    main()
