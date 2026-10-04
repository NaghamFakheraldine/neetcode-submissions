class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_length = len(nums)
        # if (nums_length < 2 or nums_length > 1000) or (target < -10000000 or target > 10000000):
        #     return []

        ## Solution 1
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             combinations = [i, j]
        #             return combinations
        # return []

        ## Solution 2
        # i = 0 
        # j = 1
        # while i < j:
        #     print(f'i = {i} | j = {j}')
        #     if nums[i] + nums[j] == target:
        #         print(f'[{i}, {j}')
        #         return [i, j]
        #     elif j < nums_length - 1:
        #         print(i)
        #         j = j + 1
        #         print(f"{j} <= {nums_length}")
        #     else:
        #         print(f"i = {i} + 1")
        #         i += 1
        #         j = i + 1
        # return []

        ## Solution 3
        # for i in range(nums_length):
        #     search_value = target - nums[i]
        #     print(f"search_value = {target} - {nums[i]} = {search_value}")
        #     if search_value in nums :
        #         nums_old = nums[i]
        #         nums[i] = search_value + target
        #         try: 
        #             search_value_index = nums.index(search_value)
        #         except ValueError:
        #             continue
        #         nums[i] = nums_old
        #         return [i, search_value_index]
        # return []

        ## Solution 4
        # indices = {}

        # for i, n in enumerate(nums):
        #     indices[n] = i
        #     print(f"indices = {indices}")

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     print(f"diff = {diff}")
        #     # print(f"indices[diff] = {indices[diff]}")
        #     # print(f"indices[diff] != i = {indices[diff] != i}")
        #     if diff in indices and indices[diff] != i:
        #         print(f"[{i}, {indices[diff]}]")
        #         return [i, indices[diff]]
        # return []

        ## Solution 5
        # hashmap = {}

        # for index, number in enumerate(nums):
        #     hashmap[number] = index
            
        # for index, number in enumerate(nums):
        #     diff = target - number
        #     if diff in hashmap and hashmap[diff] != index:
        #         return [index, hashmap[diff]]
        # return []

        ## Solution 6
        heatmap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in heatmap and heatmap[diff] != index:
                return [min(index, heatmap[diff]), max(index, heatmap[diff])]
            heatmap[number] = index
        return []
