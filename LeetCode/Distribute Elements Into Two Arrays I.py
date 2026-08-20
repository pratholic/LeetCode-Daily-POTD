class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res1 = []
        res2 = []

        res1.append(nums[0])
        res2.append(nums[1])

        for i in range(2, n):
            if res1[-1] > res2[-1]:
                res1.append(nums[i])

            else:
                res2.append(nums[i])

        return res1 + res2