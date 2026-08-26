class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        cnt = 0
        l = 0
        for r in range(n):
            cnt += 1 if s[r] == '1' else 0

            while cnt > k:
                if s[l] == '1':
                    cnt -= 1

                l += 1

            if cnt == k:
                while s[l] == '0':
                    l += 1

                cur = s[l : r + 1]

                if not ans or len(cur) < len(ans):
                    ans = cur

                elif len(cur) == len(ans):
                    ans = min(ans, cur)

        return ans