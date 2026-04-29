class Solution:
    #BRUTEFORCE APPROACH
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0  # store maximum water found

        # Try every pair of lines
        for i in range(n):
            for j in range(i + 1, n):
                
                # Width between lines
                width = j - i
                
                # Height is limited by shorter line
                h = min(height[i], height[j])
                
                # Calculate area
                area = width * h
                
                # Update maximum area
                max_area = max(max_area, area)

        return max_area
    

class Solution:
    #OPTIMAL APPROACH
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0  # stores maximum water found

        while left < right:
            # Calculate width between two pointers
            width = right - left
            
            # Water height is limited by the shorter line
            h = min(height[left], height[right])
            
            # Calculate current area
            area = width * h
            
            # Update maximum area
            max_area = max(max_area, area)

            # Move the pointer with smaller height
            # because it is the bottleneck
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area