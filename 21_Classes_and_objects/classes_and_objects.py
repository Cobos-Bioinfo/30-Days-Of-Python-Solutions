# Day 21 - 30DaysOfPython Challenge
# Classes and Objects

# Level 1
# 1 - Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
ages: list[int] = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self, data: list[int | float]) -> None:
        self.data = data.copy() # Avoid modifying original list
    
    
    def count(self) -> int:
        return len(self.data)
    
    
    def sum(self) -> float:
        return sum(self.data)
    
    
    def min(self) -> int | float:
        return min(self.data)
    
    
    def max(self) -> int | float:
        return max(self.data)
    
    # Although most of the following methods are already defined in mypackage.
    # The OOP principle of Encapsulation states that classes should use its own methods, not reach outside (e.g., to mypackage funcs).
    def range(self) -> int | float:
        return self.max() - self.min()
    
    
    def mean(self) -> float:
        return self.sum() / self.count()
    
    
    def median(self) -> float:
        sorted_data = sorted(self.data)
        n = self.count()
        if n % 2 == 1:
            return sorted_data[n//2]
        else:
            return (sorted_data[(n//2) - 1] + sorted_data[n//2]) / 2
    
    
    def mode(self) -> list[int | float]:
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        max_count = max(freq.values())
        modes = []
        for k, v in freq.items():
            if v == max_count:
                modes.append(k)
        return modes[0] if len(modes) == 1 else modes
    
    
    def var(self) -> float:
        mean = self.mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        return round(sum(squared_diffs) / self.count(), 2)
    
    
    def std(self) -> float:
        return round(self.var() ** 0.5, 2)
    
    
    def freq_dist(self) -> list[tuple[float, int | float]]:
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        total = self.count()
        # Transform the freq dict into a sorted list of tuples
        return sorted([(count / total * 100, value) for value, count in freq.items()], reverse=True)


# Level 2
# 1 - Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set() # Each item: (amount, description)
        self.expenses = set() # Each item: (amount, description)
    
    
    def total_income(self) -> float:
        return sum(income[0] for income in self.incomes)
    
    
    def total_expenses(self) -> float:
        return sum(expense[0] for expense in self.expenses)
    
    
    def add_income(self, amount: float, description: str) -> None:
        if amount <= 0:
            raise ValueError("Income amount must be positive.") # raise stops the func from running and the amount from being added.
        self.incomes.add((amount, description))
    
    
    def add_expense(self, amount: float, description: str) -> None:
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        self.expenses.add((amount, description))
    
    
    def account_balance(self) -> float:
        return self.total_income() - self.total_expenses()
    
    
    def account_info(self) -> str:
        info = (
            f"\nAccount of {self.firstname} {self.lastname}\n"
            f"----------------------------\n"
            f"Total Income: {self.total_income():.2f}\n"
            f"Total Expenses: {self.total_expenses():.2f}\n"
            f"Account Balance: {self.account_balance():.2f}\n"
            
            f"\nIncomes:\n"
        )

        for amount, desc in self.incomes:
            info += f"{amount:.2f} - {desc}\n"
        
        info += f"\nExpenses:\n"
        
        for amount, desc in self.expenses:
            info += f"{amount:.2f} - {desc}\n"
        
        return info


# USAGE EXAMPLE:
# Create an account
account: PersonAccount = PersonAccount("Alejandro", "Cobos")

# Add incomes
account.add_income(2000, "Salary")
account.add_income(300, "Side Hustle")

# Add expenses
account.add_expense(1200, "Rent")
account.add_expense(300, "Groceries")
account.add_expense(150, "Car")

# Print account info
print(account.account_info())
