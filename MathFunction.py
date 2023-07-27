from BareMathFunction import BareMathFunction
from zope import interface
from matplotlib import pyplot
import io
import base64
interface.implementer(BareMathFunction)
class mathFunction:
    def __init__(self, mathFunction: str, start: float, stop: float, step: float = 1):
        """Initialize the object with it's function"""
        self.mathFunction = mathFunction
        x=1
        try:            
            eval(self.mathFunction)
        except:
            raise ValueError("Invalid function")
        self.bytesOfSVG = io.BytesIO()
        self.pyplot = pyplot
        self.xValues = range(int(start), int(stop + 1), step)
        self.yValues = [self(x) for x in self.xValues]
        self.step = step
        
    def __call__(self, x):
        return eval(self.mathFunction)
    
    def plot(self, start: float, stop: float, step: float):
        """Plot the function from start to stop x values, autosizing the y range to fit the data"""
        pass
    
    def plot(self):
        """Plot the function from start to stop x values, autosizing the y range to fit the data"""
        self.pyplot.plot(self.xValues, self.yValues)
        self.pyplot.xlabel("x")
        self.pyplot.ylabel("y")
        
        self.pyplot.savefig(self.bytesOfSVG, format='svg', dpi=1200)
        self.bytesOfSVG.seek(0)
        imageInBase64 = base64.b64encode(self.bytesOfSVG.read()).decode()
        imageInHTMLinBase64 = f"<img src='data:image/svg+xml;base64,{imageInBase64}'/>"
        return imageInHTMLinBase64