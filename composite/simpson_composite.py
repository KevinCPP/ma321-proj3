import math
import numpy as np
from scipy.integrate import quad

class SimpsonComposite:
    def __init__(self):
        self.name = "Simpson's Rule Composite"

    def calculate(self, function, lower, upper, num_intervals):
        if num_intervals % 2 != 0:
            raise ValueError(f"Error: invalid number of intervals {num_intervals} passed to SimpsonComposite:calculate(). Must be an even number")
        
        delta_x = (upper - lower) / num_intervals

        sum_even = sum(function(lower + 2 * i * delta_x) for i in range(1, num_intervals // 2))
        sum_odd = sum(function(lower + (2 * i - 1) * delta_x) for i in range(1, num_intervals // 2 + 1))

        return (delta_x / 3) * (function(lower) + (2 * sum_even) + (4 * sum_odd) + function(upper))

    def demo(self):
        def function(x):
            return math.exp(-x) * math.cos(x)

        lower_bound = 0
        upper_bound = 2 * math.pi
        exact, _ = quad(function, lower_bound, upper_bound)

        print(f"{self.name} for f(x) = e^(-x) * cos(x):")
        for i in range(2, 10, 2):
            result = self.calculate(function, lower_bound, upper_bound, i)
            print(f"\tn={i}: {result}. Exact Result: {exact}. Difference: {result-exact}")
        
        print("")


