from types import LambdaType
from typing import Tuple, List

import numpy as np


class Line(object):
    pass


class Line:

    def __init__(self, start: Tuple[float, float], end: Tuple[float, float], color="#444444"):
        self.start = start
        self.end = end
        self.color = color
        self._linestyle = '-'
        self._linewidth = 0.75

    def linewidth(self, width: float):
        self._linewidth = width
        return self

    def linestyle(self, style: str):
        self._linestyle = style
        return self

    def plot(self, axis):
        axis.plot([self.start[0], self.end[0]], [self.start[1], self.end[1]],
                  color=self.color,
                  linewidth=self._linewidth,
                  linestyle=self._linestyle)


class Point:
    def __init__(self, x: float, y: float, color="#444444"):
        self.x = x
        self.y = y
        self.color = color


class Function:
    def __init__(self, expression: LambdaType, domains: List[Tuple[float, float]], color="#444444"):
        self.expression = expression
        self.domains = domains
        self.color = color

    def plot(self, axis):
        for domain in self.domains:
            X = np.linspace(domain[0], domain[1], 1000)
            Y = self.expression(X)
            axis.plot(X, Y, color=self.color, linestyle="-", linewidth=0.8)
