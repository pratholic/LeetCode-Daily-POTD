class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        st = ['a', 'b', 'c']
        ans = []

        def f(idx, cur):
            if idx >= n:
                ans.append(cur)
                return

            for ch in st:
                if not cur or cur[-1] != ch:
                    f(idx + 1, cur + ch)

        f(0, "")
        ans.sort()

        if k > len(ans):
            return ""

        return ans[k - 1]