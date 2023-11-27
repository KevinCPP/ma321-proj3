import math
import numpy as np
from scipy.integrate import quad

from composite.trap_composite import TrapezoidComposite

class Romberg:
    def __init__(self):
        self.name = "Romberg Integration"
        self.trapezoid = TrapezoidComposite()

    def calculate(self, function, lower, upper, depth):
        # initialize the matrix
        R = [[0 for _ in range(depth)] for _ in range(depth)]
        
        # fill in the first column
        for i in range(depth):
            num_intervals = 2 ** i
            R[i][0] = self.trapezoid.calculate(function, lower, upper, num_intervals)
        
        # Apply Richardson's Extrapolation
        for j in range(1, depth):
            for i in range(j, depth):
                R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (4 ** j - 1)

        return R

    def demo(self):
        # 1 / (1 + x)
        def fun1(x):
            return 1 / (1 + x)
        
        # e^x
        def fun2(x):
            return math.exp(x)
        
        # 4 / (1 + x^2)
        def fun3(x):
            return 4 / (1 + (x ** 2))

        lower = 0
        upper = 1
        depth = 8
        functions = [fun1, fun2, fun3]
        expressions = ["f(x) = 1 / (1 + x)", "f(x) = e^x", "f(x) = 4 / (1 + x^2)"]

        print(f"{self.name}:")
        for i, fun in enumerate(functions):
            r = self.calculate(fun, lower, upper, depth)
            print(f"    Romberg Table for {expressions[i]}:")

            # Printing each row of the Romberg table
            for row in r:
                formatted_row = ' '.join(f"{value:10.8f}" for value in row)  # Format each number in the row
                print(f"\t{formatted_row}")
            
            exact, _ = quad(fun, lower, upper)
            print(f"\tMost accurate estimate: {r[-1][-1]}. Exact Result: {exact}. Difference: {r[-1][-1]-exact}")
            print("\n")

