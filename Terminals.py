import random
from abc import ABC

from Functions import TreeNode
from TreeUtilities import TerminalNode


class InputTerminal(TerminalNode, ABC):
    pass


class FunctionTerminal(TerminalNode, ABC):
    pass


class ConstantTerminal(TerminalNode, ABC):
    pass


#########################################

class EphemeralRandomConstant(ConstantTerminal):
    def __init__(self, min_value: float = 0, max_value: float = 1):
        print('ephemeral random constant')
        self.min_value = min_value
        self.max_value = max_value
        self._constant_number = random.Random().uniform(min_value, max_value)

    def get_value(self):
        return self._constant_number

    def update(self):
        self._constant_number = random.Random().uniform(self.min_value, self.max_value)


class IndependentVariable(FunctionTerminal):
    def __init__(self, variable):
        self.variable = variable

    def get_value(self):
        pass

