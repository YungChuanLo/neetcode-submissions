class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        min_index = 0
        max_profit = 0

        
        while (index < len(prices)):
            if(max_profit < (prices[index] - prices[min_index])):
                max_profit = (prices[index] - prices[min_index])
            if(prices[index] < prices[min_index]):
                min_index =  index
            
            index += 1

        return max_profit
        