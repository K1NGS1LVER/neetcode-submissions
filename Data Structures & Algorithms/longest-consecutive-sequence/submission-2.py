class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num -1 not in num_set:
                current_sequence = 0
                current_num = num

                while current_num in num_set:

                    current_sequence += 1
                    current_num += 1

                if current_sequence > longest:
                    longest = current_sequence
        
        return longest
            

        