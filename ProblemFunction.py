from abc import ABC, abstractmethod
from typing import Tuple, List

import numpy as np
import pandas as pd


class ProblemFunction(ABC):
    def __init__(self):
        self.__variables_count = 0

    @abstractmethod
    def execute(self, x: []):
        pass

    @abstractmethod
    def get_variables_count(self):
        pass

    def generate_data(self, variables_intervals: List[Tuple[float, float]], step: float = 0.1):
        input_variables = []
        for i in range(len(variables_intervals)):
            interval = variables_intervals[i]
            interval_values = np.arange(interval[0], interval[1], step)
            input_variables.append(interval_values)

        size = 1
        for i in range(len(input_variables)):
            ndarray = input_variables[i]
            size = size * ndarray.shape[0]

        input_data = pd.DataFrame(self.__cartesian_product(input_variables))
        output_data = self.execute(input_data)
        if type(output_data) is pd.Series:
            output_data = output_data.to_frame()
        return input_data, output_data

    # from Senderle (stack over flow)
    def __cartesian_product(self, arrays: []):
        la = len(arrays)
        dtype = np.result_type(*arrays)
        arr = np.empty([la] + [len(a) for a in arrays], dtype=dtype)
        for i, a in enumerate(np.ix_(*arrays)):
            arr[i, ...] = a
        return arr.reshape(la, -1).T





class SimplePolynomialFromBook(ProblemFunction):

    def execute(self, x: []):
        return x[0] ** 2 + x[0] + 1

    def get_variables_count(self):
        return 1




