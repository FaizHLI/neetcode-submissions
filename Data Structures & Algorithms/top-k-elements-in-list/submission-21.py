class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heap
        freq = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]