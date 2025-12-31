# Base class
class BusinessUtility:
    def calculate_margin(self, revenue, cost):
        return ((revenue - cost) / revenue) * 100


# Child class (Inheritance + Method Overriding)
class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self, revenue, cost):
        regular_margin = super().calculate_margin(revenue, cost)
        return regular_margin + 10


# Profitability checker class
class ProfitabilityChecker:
    def check_profitability(self, regular_margin):
        if regular_margin >= 10:
            print("Business is profitable.")
        else:
            print("Business is not profitable.")


# Main program
revenue = float(input("Enter Revenue: "))
cost = float(input("Enter Cost: "))

regular_business = BusinessUtility()
seasonal_business = SeasonalBusinessUtility()
checker = ProfitabilityChecker()

regular_margin = regular_business.calculate_margin(revenue, cost)
seasonal_margin = seasonal_business.calculate_margin(revenue, cost)

print(f"\nRegular Margin: {regular_margin:.2f}%")
print(f"Seasonal Margin: {seasonal_margin:.2f}%")

checker.check_profitability(regular_margin)
