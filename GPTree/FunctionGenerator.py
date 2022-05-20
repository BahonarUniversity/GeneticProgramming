from abc import ABC, abstractmethod

from GPTree.Functions import AdditionFunction, ProtectedDivisionFunction, MultiplicationFunction, SubtractionFunction
from GPTree.Generator import FunctionGenerator
from GPTree.TreeUtilities import FunctionNode


class AdditionFunctionGenerator(FunctionGenerator):
    def generate(self) -> AdditionFunction:
        return AdditionFunction()


class SubtractionFunctionGenerator(FunctionGenerator):
    def generate(self) -> SubtractionFunction:
        return SubtractionFunction()


class MultiplicationFunctionGenerator(FunctionGenerator):
    def generate(self) -> MultiplicationFunction:
        return MultiplicationFunction()


class ProtectedDivisionFunctionGenerator(FunctionGenerator):
    def generate(self) -> ProtectedDivisionFunction:
        return ProtectedDivisionFunction()
