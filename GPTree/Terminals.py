import random
from abc import ABC

from GPTree.Functions import TreeNode
from GPTree.TreeUtilities import TerminalNode


class InputTerminal(TerminalNode, ABC):
    pass


class FunctionTerminal(TerminalNode, ABC):
    pass


class ConstantTerminal(TerminalNode, ABC):
    pass


#########################################

class EphemeralRandomConstant(ConstantTerminal):
    def __init__(self, min_value: float = 0, max_value: float = 1):
        self.min_value = min_value
        self.max_value = max_value
        self._constant_number = random.Random().uniform(min_value, max_value)

    def get_composition(self):
        return '%.4f' % self._constant_number

    def update(self):
        self._constant_number = random.Random().uniform(self.min_value, self.max_value)


class InputVariable(FunctionTerminal):
    def __init__(self, variable: str):
        self.variable = variable

    def get_composition(self):
        return self.variable

