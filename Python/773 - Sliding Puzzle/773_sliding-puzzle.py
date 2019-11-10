from leezy import Solution, solution
from collections import deque

class Q773(Solution):
    @solution
    def slidingPuzzle(self, board):
        # 36ms 74.15%
        def transfer(state):
            new_states = []
            idx = state.index('0')
            parts = list(state)
            v_idx = (idx + 3) % 6
            parts[idx], parts[v_idx] = parts[v_idx], parts[idx]
            new_states.append(''.join(parts))
            if idx in (0, 1, 3, 4):
                new_states.append(state[:idx]+state[idx+1]+'0'+state[idx+2:])
            if idx in (2, 1, 5, 4):
                new_states.append(state[:idx-1]+'0'+state[idx-1]+state[idx+1:])
            return new_states

        init = ''.join(''.join([str(i) for i in row]) for row in board)
        target = '123450'
        if init == target:
            return 0
        queue = deque()
        queue.append(init)
        seen = set()
        seen.add(init)
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                state = queue.popleft()
                for new_s in transfer(state):
                    if new_s == target:
                        return step
                    if new_s in seen:
                        continue
                    seen.add(new_s)
                    queue.append(new_s)
        return -1






def main():
    q = Q773()
    q.add_args([[1, 2, 3], [4, 0, 5]])
    q.add_args([[1, 2, 3], [5, 4, 0]])
    q.add_args([[4, 1, 2], [5, 0, 3]])
    q.add_args([[3, 2, 4], [1, 5, 0]])
    q.run()


if __name__ == "__main__":
    main()
