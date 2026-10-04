class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        if (nums_length < 2 or nums_length > 1000) or (target < -10000000 or target > 10000000):
            return []

        i = 0
        j = 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif j < nums_length - 1:
                j = j + 1
            else:
                i = i + 1
                j = i + 1
        return []