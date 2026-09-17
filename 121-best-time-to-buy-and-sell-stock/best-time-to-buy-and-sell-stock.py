class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max = 0
        minP = prices[0]
        for i in range(n):
            temp = prices[i] - minP
            if temp > max:
                max = temp
            if prices[i] < minP:
                minP = prices[i]
        return max
        