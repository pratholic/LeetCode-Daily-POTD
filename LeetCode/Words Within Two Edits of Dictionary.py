from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries)
        ans = []

        for cur_word in queries:
            changes = float('inf')

            for word in dictionary:
                cur_changes = 0 

                for j in range(len(word)):
                    if cur_word[j] != word[j]:
                        cur_changes += 1

                changes = min(changes, cur_changes)

            if changes <= 2:
                ans.append(cur_word)

        return ans