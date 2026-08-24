class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums) - 1

        while l < r:
            mid = l + (r - l)//2 

            # if mid is bigger means mid is in the bigger array 
            # so search only in the right sub array 
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            # works only in rotated array

        return nums[l]
    
        
