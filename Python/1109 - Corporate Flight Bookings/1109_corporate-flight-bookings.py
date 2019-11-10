from leezy import Solution, solution


class Q1109(Solution):
    @solution
    def corpFlightBookings(self, bookings, n):
        # 
        # insts[0] is for 1-based index flights collections
        # insts[n+1] is for booking label-n flight
        insts = [0] * (n+2)
        for i, j, k in bookings:
            insts[i] += k
            insts[j+1] -= k
        ans = [0] * (n + 1)
        for i in range(1, n+1):
            ans[i] = ans[i-1] + insts[i]
        return ans[1:]

    @solution
    def booking_concise(self, bookings, n):
        # 980ms 87.80%
        insts = [0] * (n+1)
        for i, j, k in bookings:
            insts[i-1] += k
            insts[j] -= k

        for i in range(1, n+1):
            insts[i] += insts[i-1]
        return insts[:-1]



def main():
    q = Q1109()
    q.add_args([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
    q.run()


if __name__ == "__main__":
    main()
