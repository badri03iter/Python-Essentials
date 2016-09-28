def max_profitt(prices):
    buy=prices[0]
    sell=prices[0]
    profit=sell-buy
    max_profit = profit

    for curr in prices:
        profit = curr-buy

        if profit > max_profit:
            sell=curr
            max_profit=profit
        else:
            buy=curr
    return max_profit

#prices=[12,11,15,3,10,21,-1]
prices =[30,22,21,5]
print max_profitt(prices)