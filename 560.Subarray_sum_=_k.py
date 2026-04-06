class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #BRUTEFORCE APPROACH
        count = 0
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                
                if curr_sum == k:
                    count += 1

        return count
    
#___________________________________________________________________________________
#PREFIX SUM APPROACH
#___________________________________________________________________________________
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0              # Stores number of subarrays with sum = k
        curSum = 0           # Running prefix sum
        
        # Dictionary to store prefix sum frequencies
        # {prefix_sum : count}
        # Initialize with {0:1} to handle cases where subarray starts from index 0
        prefixSums = {0: 1}

        for n in nums:
            # Update running prefix sum
            curSum += n
            
            # We check if there exists a prefix sum such that:
            # current_sum - previous_sum = k
            # => previous_sum = current_sum - k
            diff = curSum - k

            # If diff exists, we found subarray(s) ending here with sum = k
            res += prefixSums.get(diff, 0)

            # Store current prefix sum in hashmap
            # Increment frequency if already exists
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res