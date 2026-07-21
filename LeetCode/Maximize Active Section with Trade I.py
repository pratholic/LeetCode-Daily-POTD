class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)

        initial = s.count('1')
        ans = initial

        i = 0
        while i < n:
            j = i

            while j < n and t[j] == t[i]:
                j += 1

            if t[i] == '1' and i > 0 and j < n and t[i - 1] == '0' and t[j] == '0':

                l = i - 1
                while l >= 0 and t[l] == '0':
                    l -= 1

                left_zero = i - l - 1

                r = j
                while r < n and t[r] == '0':
                    r += 1

                right_zero = r - j

                ans = max(ans, initial + left_zero + right_zero)

            i = j

        return ans