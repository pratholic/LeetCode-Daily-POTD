class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        all_odd = all(x & 1 for x in nums1)
        all_even = all(x & 1 == 0 for x in nums1)

        if all_odd or all_even:
            return True

        mn = min(nums1)
        
        return mn % 2 == 1