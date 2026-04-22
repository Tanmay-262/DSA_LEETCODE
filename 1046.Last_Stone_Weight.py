class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max-heap banane ke liye negatives use kiye
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        
        # jab tak 2 stones hain
        while len(maxheap) > 1:
            # 2 sabse bade stones nikale
            st1 = heapq.heappop(maxheap)
            st2 = heapq.heappop(maxheap)
            
            # equal hain toh skip
            if st1 == st2:
                continue
            
            # difference wapas heap mein daalo
            heapq.heappush(maxheap, -abs(st1 - st2))
        
        # agar empty hai toh 0
        if len(maxheap) == 0:
            return 0
        
        # last stone return (positive)
        return abs(maxheap[0])