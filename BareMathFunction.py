import zope.interface

class BareMathFunction(zope.interface.Interface):
    mathFunction = zope.interface.Attribute("The function to be plotted")
    def __init__(self, mathFunction: str):
        """Initialize the function with any parameters"""
        pass
    def __call__(x):
        """Return the value of the function at x"""
        pass
    def plot(self, start: float, stop: float):
        """Plot the function from start to stop"""
        pass