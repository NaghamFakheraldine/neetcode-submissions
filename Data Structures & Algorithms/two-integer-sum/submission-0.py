class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        if (nums_length < 2 or nums_length > 1000) or (target < -10000000 or target > 10000000):
            return []

        for i in range(nums_length):
            if nums[i] < -10000000 or nums[i] > 10000000:
                return []
            for j in range(i + 1, nums_length):
                if nums[i] + nums[j] == target:
                    combinations = [i, j]
                    return combinations
        return []