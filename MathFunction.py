from BareMathFunction import BareMathFunction
from zope import interface
from matplotlib import pyplot
import io
import base64
interface.implementer(BareMathFunction)
class mathFunction:
    def __init__(self, mathFunction: str):
        """Initialize the object with it's function"""
        self.mathFunction = mathFunction
        x=1
        try:            
            eval(self.mathFunction)
        except:
            raise ValueError("Invalid function")
    def __call__(self, x):
        return eval(self.mathFunction)
    
    def plot(self, start: float, stop: float, step: float):
        """Plot the function from start to stop x values, autosizing the y range to fit the data"""
        pass
    
    def plot(self, start: float, stop: float):
        """Plot the function from start to stop x values, autosizing the y range to fit the data"""
        step = 1
        xValues = range(int(start), int(stop + 1), step)
        yValues = [self(x) for x in xValues]
        pyplot.plot(xValues, yValues)
        pyplot.xlabel("x")
        pyplot.ylabel("y")
        returnSVG = io.BytesIO()
        pyplot.savefig(returnSVG, format='svg', dpi=1200)
        returnSVG.seek(0)
        returnB64 = base64.b64encode(returnSVG.read()).decode()
        returnHTML = f"<img src='data:image/svg+xml;base64,{returnB64}'/>"
        return returnHTML