from composite.simpson_composite import SimpsonComposite
from composite.trap_composite import TrapezoidComposite

def demo_composite():
    simpson = SimpsonComposite()
    trapezoid = TrapezoidComposite()
    
    simpson.demo()
    trapezoid.demo()
