class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans = 0

        def check(num):
            num = str(num)
            ans = 0

            if len(num) < 3:
                return 0

            for i in range(1, len(num) - 1):
                if (num[i - 1] < num[i] > num[i + 1]) or (num[i - 1] > num[i] < num[i + 1]):
                    ans += 1

            return ans

        for num in range(num1, num2 + 1):

            ans += check(num)

        return ans