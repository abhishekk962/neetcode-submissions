class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, num in enumerate(nums):
            if num not in hm:
                hm[target-num] = i
            else:
                return [hm[num], i]