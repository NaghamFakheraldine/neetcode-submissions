class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        if (nums_length < 2 or nums_length > 1000) or (target < -10000000 or target > 10000000):
            return []

        for i in range(nums_length):
            search_value = target - nums[i]
            print(f"search_value = {target} - {nums[i]} = {search_value}")
            if search_value in nums :
                nums_old = nums[i]
                nums[i] = search_value + 1
                try: 
                    search_value_index = nums.index(search_value)
                except ValueError:
                    continue
                nums[i] = nums_old
                return [i, search_value_index]
        return []
