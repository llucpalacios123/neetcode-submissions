class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        result = 0
        max_result = 0

        while left < right:
            result = (right - left) * min(heights[left], heights[right])
            
            if result>max_result:
                max_result = result
            
            if heights[left] > heights[right]:
                
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else: 
                left += 1

        
        return max_result
            