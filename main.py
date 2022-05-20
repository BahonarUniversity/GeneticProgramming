# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from GPTree.FunctionGenerator import AdditionFunctionGenerator, SubtractionFunctionGenerator, MultiplicationFunctionGenerator, \
    ProtectedDivisionFunctionGenerator
from ProblemFunction import SimplePolynomialFromBook
from SimpleGeneticProgramming import SimpleGeneticProgramming
from GPTree.TerminalGenerator import EphemeralRandomConstantGenerator, InputVariableGenerator


def run_genetic_programming():
    functions = [AdditionFunctionGenerator(), SubtractionFunctionGenerator(), MultiplicationFunctionGenerator(),
                 ProtectedDivisionFunctionGenerator()]
    terminals = [EphemeralRandomConstantGenerator(), InputVariableGenerator('X[0]')]
    sgp = SimpleGeneticProgramming(n_population=4, trees_depth=2, function_set=functions, terminal_set=functions)
    sf = SimplePolynomialFromBook()
    input_data, output_data = sf.generate_data([(-5, 5)], 0.1)
    sgp.train(input_data, output_data)


if __name__ == '__main__':
    run_genetic_programming()

