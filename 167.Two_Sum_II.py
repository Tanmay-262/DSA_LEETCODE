from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted array that sum to the target.

        Args:
            numbers: Sorted array of integers in ascending order
            target: Target sum to find

        Returns:
            List containing 1-indexed positions of the two numbers
        """
        n = len(numbers)

        # Iterate through each number as the first element
        for i in range(n - 1):
            # Calculate the complement needed to reach the target
            complement = target - numbers[i]

            # Binary search template to find first index where numbers[mid] >= complement
            left, right = i + 1, n - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] >= complement:
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            # Check if the complement exists at the found position
            if first_true_index != -1 and numbers[first_true_index] == complement:
                # Return 1-indexed positions
                return [i + 1, first_true_index + 1]

        return []  # Problem guarantees a solution exists
    
#------------------------------------------------------------------
#OPTIMAL APPROACH: Two Pointers
#------------------------------------------------------------------
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]  # 1-based index
            
            elif curr_sum < target:
                left += 1   # need bigger sum
            
            else:
                right -= 1  # need smaller sum

        return []