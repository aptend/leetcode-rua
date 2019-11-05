from leeyzer import solution, Solution


class Q1227(Solution):
    @solution
    def nthPersonGetsNthSeat(self, n):
        # 536ms 14.41%
        # n = 6
        # ans = 
        #  1 / 6  # first person takes nth seat
        #  + 1 / 6 * 1 / 5 # 1st takes 2nd's seat, and 2nd takes the nth seat
        #  + 1 / 6 * 1 / 5 * 1 / 4 # 1st takes 2nd's, 2nd takes 3rd's, 3rd takes nth
        #  + 1 / 6 + 1 / 4 # 1st takes 3rd's, 2nd takes his own, 3rd takes nth
        #  + ...
        if n == 1:
            return 1.0
        ans = 1 / n
        p = 1
        # ans_k means the nth seat is occupied by kth person
        for k in range(n-1, 1, -1):
            ans += p / (k*n)
            p *= (k+1) / k
        return 1 - ans
    
    @solution
    def nth(self, n):
        return 1.0 if n == 1 else 0.5




def main():
    q = Q1227()
    q.add_args(1)
    q.add_args(2)
    q.add_args(3)
    q.add_args(4)
    q.add_args(5)
    q.add_args(6)
    q.run()

if __name__ == '__main__':
    main()
