class Solution:
    def generateString(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)

        length = n + m - 1
        word = ['$'] * length

        can_change = [False] * length

        for i in range(n):
            if s1[i] == 'T':
                idx = i

                for j in range(m):
                    if word[idx] != '$' and word[idx] != s2[j]:
                        return ""

                    word[idx] = s2[j]
                    idx += 1

        for i in range(length):
            if word[i] == '$':
                word[i] = 'a'
                can_change[i] = True

        def is_same(start):
            for j in range(m):
                if word[start] != s2[j]:
                    return False

                start += 1

            return True


        for i in range(n):
            if s1[i] == 'F':
                
                if is_same(i):

                    changed = False
                    for k in range(i + m - 1, i - 1, -1):
                        if can_change[k]:
                            word[k] = 'b'
                            changed = True
                            break

                
                    if not changed:
                        return ""

        return "".join(word)