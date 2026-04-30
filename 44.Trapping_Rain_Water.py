class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Arrays to store max height from left and right
        max_left = [0] * n
        max_right = [0] * n

        # Fill max_left
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        # Fill max_right
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # Calculate trapped water
        water = 0
        for i in range(n):
            # Water level is limited by smaller boundary
            level = min(max_left[i], max_right[i])

            # Add water if possible
            water += level - height[i]

        return water