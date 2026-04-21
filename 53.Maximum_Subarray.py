#----------------------------------
#FIRST APPROACH
#----------------------------------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')   # store the best sum found so far
        current_sum = 0           # running sum

        for n in nums:
            current_sum += n      # keep adding elements

            # update max if current sum is better
            if current_sum > max_sum:
                max_sum = current_sum

            # if sum becomes negative, reset (fresh start)
            if current_sum < 0:
                current_sum = 0

        return max_sum
#----------------------------------
#OPTIMAL APPROACH and CLEANER CODE
#----------------------------------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with first element
        current_sum = nums[0]   # max subarray sum ending at current position
        max_sum = nums[0]       # overall maximum subarray sum

        # Traverse from second element
        for n in nums[1:]:
            # Decide: start new subarray OR extend previous one
            # If current_sum is negative, starting fresh is better
            current_sum = max(n, current_sum + n)

            # Update global maximum if needed
            max_sum = max(max_sum, current_sum)

        return max_sum