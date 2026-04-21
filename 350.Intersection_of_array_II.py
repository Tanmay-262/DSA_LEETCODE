#--------------------------------------------------
#BRUTEFORCE SOLUTION
#--------------------------------------------------
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for n in nums1:
            if n in nums2:           # O(n) search
                result.append(n)
                nums2.remove(n)      # remove to avoid reuse
        
        return result
    
#--------------------------------------------------
#HASHMAP SOLUTION
#--------------------------------------------------
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}   # stores element -> count from nums1
        
        # Step 1: Count frequency of nums1
        for n in nums1:
            freq[n] = freq.get(n, 0) + 1
        
        result = []
        
        # Step 2: Traverse nums2 and match
        for n in nums2:
            # If element exists and count > 0
            if n in freq and freq[n] > 0:
                result.append(n)
                freq[n] -= 1   # decrease count (important!)
        
        return result