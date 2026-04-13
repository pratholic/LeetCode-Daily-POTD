class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        def get_coord(i):
            return (i // 6),  (i % 6)

        def get_dist(p1, p2):
            x1, y1 = get_coord(p1)
            x2, y2 = get_coord(p2)

            return abs(x1 - x2) + abs(y1 - y2)

        dp = [[[-1] * 26 for _ in range(26)] for _ in range(n)]

        def f(idx, f1, f2):
            if idx >= n:
                return 0

            if f1 != -1 and f2 != -1 and dp[idx][f1][f2] != -1:
                return dp[idx][f1][f2]

            cur_ch = ord(word[idx]) - ord('A') # cur ch

            if f1 == -1 and f2 == -1: # first case jab dono use ho skte hai
                return f(idx + 1, cur_ch, f2)

            if f2 == -1: # f1 toh first time mein used hai, toh ab f2 ko and f1 dono ko compare karlo
                move_f2 = 0 + f(idx + 1, f1, cur_ch)

                move_f1 = get_dist(f1, cur_ch) + f(idx + 1, cur_ch, f2)

                dp[idx][f1][f2] = min(move_f2, move_f1)
                return dp[idx][f1][f2]

            move_f1 = get_dist(f1, cur_ch) + f(idx + 1, cur_ch, f2)
            move_f2 = get_dist(f2, cur_ch) + f(idx + 1, f1, cur_ch)

            dp[idx][f1][f2] = min(move_f2, move_f1)
            return dp[idx][f1][f2]

        return f(0, -1, -1)