from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        right_same = [0] * n

        j = m - 1
        matched = 0

        for i in range(n - 1, -1, -1):

            if j >= 0 and word1[i] == word2[j]:
                matched += 1
                j -= 1

            right_same[i] = matched

        seq = []
        change_power = True

        i = 0
        j = 0

        while i < n and j < m:
            if word1[i] == word2[j]:
                seq.append(i)
                j += 1

            elif change_power and (i + 1) < n and right_same[i + 1] >= m - j - 1:
                seq.append(i)
                j += 1
                change_power = False

            i += 1

        return seq if j == m else []