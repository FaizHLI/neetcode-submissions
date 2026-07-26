class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #can store tuples in  heap of the num then the freq, sort by the second index
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        heap = []
        for num in freq:
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        
