from types import LambdaType
from typing import Tuple, List

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from line import Line, Point, Function


class Graph:
    def __init__(self):
        self.ticks = []

        self.lines: List[Line] = []
        self.points: List[Point] = []
        self.functions: List[Function] = []

        self.figure: Figure = None
        self.axis = None

    def plot(self):
        figure: Figure = plt.figure(figsize=(6, 3))
        self.figure = figure

        self.axis = figure.add_axes((0.1, 0.1, 0.8, 0.8))

        self.axis.spines['right'].set_color('none')
        self.axis.spines['top'].set_color('none')
        self.axis.spines['bottom'].set_position(('data', 0))
        self.axis.spines['left'].set_position(('data', 0))

        self.plotLine()
        self.plotPoint()

        for function in self.functions:
            function.plot(self.axis)

    def addLine(self, x: Tuple[float, float], y: Tuple[float, float]):
        line = Line(x, y)
        self.lines.append(line)
        return line

    def addPoint(self, x: float, y: float):
        self.points.append(Point(x, y))

    def addFunction(self, expression: LambdaType, domain: List[Tuple[float, float]], color="#444444"):
        self.functions.append(Function(expression, domain, color))

    def addCoordinatePoint(self, x: float, y: float):
        self.points.append(Point(x, y))
        self.addLine((x, 0), (x, y)).linewidth(0.5).linestyle('--')
        self.addLine((0, y), (x, y)).linewidth(0.5).linestyle('--')

    def plotLine(self):
        for line in self.lines:
            line.plot(self.axis)

    def plotPoint(self):
        for point in self.points:
            self.axis.scatter([point.x], [point.y], color=point.color)

    def show(self):
        plt.show()
