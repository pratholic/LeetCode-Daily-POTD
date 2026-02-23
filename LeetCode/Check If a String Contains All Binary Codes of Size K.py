class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        st = set()
        unique = 1 << k

        for i in range(k, n + 1):
            sub = s[i - k:i]
            if sub not in st:
                st.add(sub)
                unique -= 1

            if unique == 0:
                return True

        return False