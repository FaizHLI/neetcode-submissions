# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #put all nodes in a heap and then iterate linking them in that order
        heap = []
        heapq.heapify(heap)
        for arr in lists:
            if arr is not None:
                heapq.heappush(heap, NodeWrapper(arr))
        head = ListNode(0)
        cur = head
        while heap:
            temp = heapq.heappop(heap)
            cur.next = temp.node
            cur = cur.next
            if temp.node.next:
                heapq.heappush(heap, NodeWrapper(temp.node.next))
        return head.next






