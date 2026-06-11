class Solution:
    def maxArea(self, heights: List[int]) -> int:

        biggest = 0
        l = 0
        r = len(heights) -1 

        while l < r:
            current_vol = min(heights[l] , heights[r]) * (r - l)
            if biggest < current_vol:
                biggest = current_vol
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return biggest
        