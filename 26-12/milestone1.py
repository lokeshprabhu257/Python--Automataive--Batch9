class StockAnalyzer:
    def __init__(self, prices):
        self.prices = prices

    def calculate_max_profit(self):
        min_price = self.prices[0]
        max_profit = 0

        for price in self.prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    def calculate_volatility_index(self):
        total_diff = 0

        for i in range(1, len(self.prices)):
            total_diff += abs(self.prices[i] - self.prices[i - 1])

        return total_diff / (len(self.prices) - 1)


# -------- Main --------
prices_input = input("Enter stock prices separated by space: ")
prices = list(map(int, prices_input.split()))

analyzer = StockAnalyzer(prices)

print("Max Profit:", analyzer.calculate_max_profit())
print("Volatility Index:", format(analyzer.calculate_volatility_index(), ".2f"))
