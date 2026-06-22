class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)

        mp = [0] * 26
        t = "balloon"

        for ch in text:
            mp[ord(ch) - ord('a')] += 1

        ans = 0

        while True:
            can_make = True

            for ch in t:
                if mp[ord(ch) - ord('a')] == 0:
                    can_make = False
                    break

                else:
                    mp[ord(ch) - ord('a')] -= 1

            if can_make:
                ans += 1

            else:
                break

        return ans