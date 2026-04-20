#BRUTEFORCE TECHNIQUE
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #BRUTEFORCE TECHNIQUE
        #in this we basically count the occurence of each element
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        freq = {}
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
            if freq[n] > len(nums) // 2:
                return n
            
#--------------------------------------------------------------------------------
#HASHMAP TECHNIQUE
#--------------------------------------------------------------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #HASHMAP TECHNIQUE
        #in this we basically count the occurence of each element using hashmap
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        freq = {}  # stores element -> count

        for n in nums:
            freq[n] = freq.get(n, 0) + 1  # increment frequency

            # as soon as we cross n//2, return
            if freq[n] > len(nums) // 2:
                return n
            
#--------------------------------------------------------------------------------
#BOYER MOORE VOTING ALGORITHM   
#--------------------------------------------------------------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #BOYER MOORE VOTING ALGORITHM
        #in this we basically maintain a candidate and a count
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        count = 0          # Tracks "vote balance"
        candidate = None   # Current majority candidate

        for num in nums:
            # If count drops to 0, we choose a new candidate
            if count == 0:
                candidate = num

            # If current number matches candidate → increase count
            if num == candidate:
                count += 1
            else:
                # If different → cancel out one occurrence
                count -= 1

        # Since problem guarantees a majority element,
        # the final candidate is the answer
        return candidate