def maxProfit(prices):
    """
    Simple One Pass

    Intuition:
        The basic idea here is to iterate over the prices and sum up all the profitable consecutive differences. This is because to get the maximum, we want to capture every opportunity where the price increases.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    total_profit = 0
    
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, we have a profit opportunity
        if prices[i] > prices[i - 1]:
            # Accumulate the profit from this opportunity
            total_profit += prices[i] - prices[i - 1]
    
    return total_profit

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)
print(ans)  # Output: 7