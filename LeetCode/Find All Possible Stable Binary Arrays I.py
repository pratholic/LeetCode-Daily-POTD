class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = (10 ** 9) + 7
        
        dp = {}
        def f(zeros, ones, last_one):
            if zeros == 0 and ones == 0:
                return 1

            state = (zeros, ones, last_one)
            if state in dp:
                return dp[state]

            res = 0
            if last_one:
                for length in range(1, min(zeros, limit) + 1):
                    res += f(zeros - length, ones, False)

            else:
                for length in range(1, min(ones, limit) + 1):
                    res += f(zeros, ones - length, True)

            dp[state] = res
            return dp[state]

        return (f(zero, one, True) + f(zero, one, False)) % MOD