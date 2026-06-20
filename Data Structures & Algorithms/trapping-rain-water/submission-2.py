class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return -1
        
        res = 0
        n = len(height)
        l_arr = [0] * n
        r_arr = [0] * n
        res_arr= [0] * n

        for i,num in enumerate(height):
            if i == 0:
                l_arr[0] = height[0]
                continue
            l_arr[i] = max(l_arr[i - 1] , height[i - 1])
        
        for i, num in reversed(list(enumerate(height))):
            if i == n-1:
                r_arr[n-1]=height[n-1]
                continue
            r_arr[i] = max(r_arr[i+1] , height[i+1])
        
        for i,num in enumerate(height):
            res_arr[i] = min(r_arr[i] , l_arr[i]) - height[i]
            if res_arr[i] > 0:
                res += res_arr[i]
        
        return res


        

        