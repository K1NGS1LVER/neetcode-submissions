class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for i in matrix:
            for j in i:
                nums.append(j)
        # naive brute force approach

        n = len(nums)

        l , r = 0 , n - 1

        while l <= r:
            mid = (r + l)//2 

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return False