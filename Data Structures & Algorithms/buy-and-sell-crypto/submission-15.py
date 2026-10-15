class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        #naive: 
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
        return maxP
            