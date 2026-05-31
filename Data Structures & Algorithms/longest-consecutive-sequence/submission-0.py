class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current_sequence = 0
            current_num = num

            while current_num in nums:
                current_sequence += 1
                current_num += 1

            if current_sequence > longest:
                longest = current_sequence
        
        return longest
            

        