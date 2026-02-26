class Solution:
    def numSteps(self, s: str) -> int:
        
        original_num = 0
        s = s[::-1]
        for i, v in enumerate(s):
            if v == '1':
                original_num += (1 << i)

        if original_num == 1:
            return 0

        ans = 0
        while original_num != 1:
            if original_num & 1:
                original_num += 1

            else:
                original_num //= 2

            ans += 1

        return ans