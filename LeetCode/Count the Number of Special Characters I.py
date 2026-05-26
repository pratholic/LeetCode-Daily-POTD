class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        ans = 0

        lowers = [0] * 26
        uppers = [0] * 26

        for ch in word:
            if 'a' <= ch <= 'z':
                lowers[ord(ch) - ord('a')] += 1

            if 'A' <= ch <= 'Z':
                uppers[ord(ch) - ord('A')] += 1


        for i in range(26):
            if lowers[i] != 0 and uppers[i] != 0:
                ans += 1

        return ans