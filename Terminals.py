from abc import ABC, abstractmethod

from Functions import TreeNode
from TreeUtilities import TerminalNode, Arguments


class InputTerminal(TerminalNode, ABC):
    pass


class FunctionTerminal(TerminalNode, ABC):
    pass


class ConstantTerminal(TerminalNode, ABC):
    pass


#########################################

class EphemeralRandomConstant(ConstantTerminal):
    def __init__(self):


    def get_value(self, arguments: Arguments):
        pass