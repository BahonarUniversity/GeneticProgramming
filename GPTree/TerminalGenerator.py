from GPTree.Generator import TerminalGenerator
from GPTree.Terminals import EphemeralRandomConstant, InputVariable


class EphemeralRandomConstantGenerator(TerminalGenerator):
    def generate(self) -> EphemeralRandomConstant:
        return EphemeralRandomConstant(-5, 5)


class InputVariableGenerator(TerminalGenerator):
    def __init__(self, variable_name: str = 'x'):
        self.__variable = variable_name

    def generate(self) -> InputVariable:
        return InputVariable(self.__variable)
