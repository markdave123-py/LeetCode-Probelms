class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        s = 0 #slow pointer -> to buy
        f = 1 #fast pointer -. to sell

        maxProfit = 0

        while(f < len(prices)):
            if prices[f] < prices[s]:
                s = f
                

            else:
                profit = prices[f] - prices[s]
                maxProfit = max(profit, maxProfit)
                
            f += 1

        return 
    

p = {5:6}
print(p[5])
