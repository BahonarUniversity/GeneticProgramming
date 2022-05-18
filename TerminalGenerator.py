from Generator import TerminalGenerator
from Terminals import EphemeralRandomConstant, IndependentVariable


class EphemeralRandomConstantGenerator(TerminalGenerator):
    def generate(self) -> EphemeralRandomConstant:
        return EphemeralRandomConstant(-5, 5)


class IndependentVariableGenerator(TerminalGenerator):
    def generate(self) -> IndependentVariable:
        return IndependentVariable('variable')
