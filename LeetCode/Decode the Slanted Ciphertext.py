class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if rows == 1:
            return encodedText

        cols = n // rows

        grid = [[''] * cols for _ in range(rows)]

        idx = 0
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = encodedText[idx]
                idx += 1

        ans = []
        for col in range(cols):
            i = 0
            j = col

            while i < rows and j < cols:
                ans.append(grid[i][j])
                i += 1
                j += 1

        return "".join(ans).rstrip()