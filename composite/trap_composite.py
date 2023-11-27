import math
import numpy as np
from scipy.integrate import quad

class TrapezoidComposite:
    def __init__(self):
        self.name = "Trapezoid Rule Composite"

    def calculate(self, function, lower, upper, num_intervals):
        delta_x = (upper - lower) / num_intervals

        sum_midpoints = sum(function(lower + i * delta_x) for i in range(1, num_intervals))

        return (delta_x / 2) * (function(lower) + 2 * sum_midpoints + function(upper))

    def demo(self):
        def function(x):
            return math.exp(-x) * math.cos(x)

        lower_bound = 0
        upper_bound = 2 * math.pi
        exact, _ = quad(function, lower_bound, upper_bound)

        print(f"{self.name}: for f(x) = e^(-x) * cos(x)")
        for i in range(2, 10, 2):
            result = self.calculate(function, lower_bound, upper_bound, i)
            print(f"\tn={i}: {result}. Exact Result: {exact}. Difference: {result-exact}")
        
        print("")
