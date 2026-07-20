class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0 
        n = len(heights)
        
        for i in range(len(heights)):
            left = i
            right = i

            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1
            
            while right < n - 1 and heights[right + 1] >= heights[i]:
                right += 1
            
            rect_length = right - left + 1
            rect_area = rect_length * heights[i]
            largest = max(largest, rect_area)
        
        return largest
        