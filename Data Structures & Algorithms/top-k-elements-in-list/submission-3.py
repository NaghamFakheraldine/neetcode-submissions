class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create a hash containing number and frequency
        {
            number: frequency
        }

        in our example:

        nums = [1,2,2,3,3,3], k = 2 
        k -> number of elements in the final list

        {
            1: 0
            2: 0
            3: 0
            }

            for n in nums update the frequency of the number in the hash
            {
                1: 1
                2: 2
                3: 3
            }

        sort the hash by the frequency
        {
            {1: 1}, {2: 2}, {3: 3}
        }

        return the top k elements from the sorted hash
        {
            {1: 1}, {2: 2}
        }

        """
        unique_numbers_set = set(nums)
        unique_numbers_hash = {}
        frequent_numbers_list = []

        # print('unique_numbers_set', unique_numbers_set)

        for i in unique_numbers_set:
            unique_numbers_hash[i] = 0

        # print('unique_numbers_hash', unique_numbers_hash)
        
        for i in nums:
            unique_numbers_hash[i] += 1
 
        # print('unique_numbers_hash', unique_numbers_hash)

        sorted_k_numbers = sorted(unique_numbers_hash.values())[len(unique_numbers_hash)-k:]
        
        # print('sorted_k_numbers', sorted_k_numbers)

        for key, value in unique_numbers_hash.items():
            if value in sorted_k_numbers:
                frequent_numbers_list.append(key)
        
        # print('frequent_numbers_list', frequent_numbers_list)

        return frequent_numbers_list