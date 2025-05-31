def maxProfit(prices):
    """
    One Pass Approach

    Intuition:
        We can maintain a running track of the minimum price so far and compute the potential profit for each day by subtracting the current price from this minimum price. This allows us to determine the maximum profit in a single pass through the array.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    max_profit = 0
    min_price = float('inf')
    
    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
            
        # Calculate current potential profit by selling at the current price
        profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit
        
    return max_profit

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)
print(ans)  # Output: 5