class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) < 2:
            return 0
        
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < buy:
                buy = price
                sell = price
            elif price > sell:
                sell = price
                max_profit = max(max_profit, sell - buy)
        
        return max_profit
