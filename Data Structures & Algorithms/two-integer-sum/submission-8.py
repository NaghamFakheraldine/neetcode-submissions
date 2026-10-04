class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        heatmap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in heatmap and heatmap[diff] != index:
                return [min(index, heatmap[diff]), max(index, heatmap[diff])]
            heatmap[number] = index
        return []
