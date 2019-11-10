from leezy import Solution, solution


class Q03(Solution):
    @solution
    def robot(self, command, obstacles, x, y):
        # 88ms
        path = set()
        cx, cy = 0, 0
        for cmd in command:
            if cmd == 'U':
                cy += 1
            else:
                cx += 1
            path.add((cx, cy))

        # eliminate points that are beyond the final point
        obs = set()
        for p in obstacles:
            if p[0] <= x and p[1] <= y:
                obs.add(tuple(p))
        
        # every round, we will move cx and cy units to up-right direction
        while x >= 0 and y >= 0:
            if len(path & obs) > 0:
                return False
            if (x, y) in path:
                return True
            # now we are more close to final point
            x, y = x - cx, y - cy
            # forget those obstacles we've passed
            new_obs = set()
            for ox, oy in obs:
                if ox > cx or oy > cy:
                    new_obs.add((ox-cx, oy-cy))
            obs = new_obs
        # no luck to touch the terminal
        return False
    



def main():
    q = Q03()
    q.add_args('URR', [], 3, 2) # True
    q.add_args('URR', [[2, 2]], 3, 2) # False
    q.add_args('URR', [[4, 2]], 3, 2) # True


    q.run()


if __name__ == "__main__":
    main()
