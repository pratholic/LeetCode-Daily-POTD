class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        result = ""
        mid_char = '$'

        n = len(s)
        half = n // 2

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        odd_count = 0

        for i in range(26):
            if count[i] % 2 == 1:
                odd_count += 1
                mid_char = chr(ord('a') + i)

        if odd_count > 1:
            return ""

        half_count = [0] * 26

        for i in range(26):
            half_count[i] = count[i] // 2

        def solve(curr, i, greater):
            nonlocal result

            if i == half:

                left_half = ''.join(curr)

                right_half = left_half[::-1]

                candidate = left_half

                if mid_char != '$':
                    candidate += mid_char

                candidate += right_half

                if candidate > target:
                    result = candidate
                    return True

                return False

            for c in range(26):

                if half_count[c] == 0:
                    continue

                ch = chr(ord('a') + c)

                if not greater and ch < target[i]:
                    continue

                curr.append(ch)
                half_count[c] -= 1

                is_greater = greater or (ch > target[i])

                if solve(curr, i + 1, is_greater):
                    return True

                curr.pop()
                half_count[c] += 1

            return False

        curr = []

        solve(curr, 0, False)

        return result