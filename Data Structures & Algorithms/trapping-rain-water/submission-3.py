from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        l_arr = [0] * n
        r_arr = [0] * n
        
        # we skip the edges as water spills
        l_arr[0] = height[0]
        for i in range(1, n):
            l_arr[i] = max(l_arr[i - 1], height[i])
        
        
        r_arr[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            r_arr[i] = max(r_arr[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(l_arr[i], r_arr[i]) - height[i]
            
        return res