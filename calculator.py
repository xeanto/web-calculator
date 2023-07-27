from flask import Flask, request, jsonify
from matplotlib import pyplot
import numpy
from MathFunction import mathFunction
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/operations/add', methods=['GET'])
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = jsonify({'result': num1 + num2})
    return result

@app.route('/operations/subtract', methods=['GET'])
def subtract():
    number = int(request.args.get('number'))
    difference = int(request.args.get('difference'))
    result = jsonify({'result': number - difference})
    return result

@app.route('/operations/multiply', methods=['GET'])
def multiply():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = jsonify({'result': num1 * num2})
    return result

@app.route('/operations/divide', methods=['GET'])
def divide():
    dividend = int(request.args.get('dividend'))
    divisor = int(request.args.get('divisor'))
    result = jsonify({'result': round(dividend / divisor,2)})
    return result

@app.route('/operations/plot', methods=['GET'])
def plot():
    preParseMathFunction = request.args.get('mathFunction')
    start = float(request.args.get('start'))
    stop = float(request.args.get('stop'))
    plottingFunction = mathFunction(preParseMathFunction, start, stop)
    return plottingFunction.plot()

@app.route('/test/mathFunction', methods=['GET'])
def testMathFunction():
    preParseMathFunction = str(request.args.get('mathFunction'))
    mathFunctionInstance = mathFunction(preParseMathFunction)
    return jsonify({'result': mathFunctionInstance(4861)})