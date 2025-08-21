# Day 21 - 30DaysOfPython Challenge
# Classes and Objects

from mypackage import arithmetic

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
        