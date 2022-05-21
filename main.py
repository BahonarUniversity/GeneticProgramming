# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from GPTree.FunctionGenerator import AdditionFunctionGenerator, SubtractionFunctionGenerator, MultiplicationFunctionGenerator, \
    ProtectedDivisionFunctionGenerator
from ProblemFunction import SimplePolynomialFromBook
from SimpleGeneticProgramming import SimpleGeneticProgramming
from GPTree.TerminalGenerator import EphemeralRandomConstantGenerator, InputVariableGenerator


def run_genetic_programming():
    np.seterr(all='raise')
    functions = [AdditionFunctionGenerator(), SubtractionFunctionGenerator(), MultiplicationFunctionGenerator(),
                 ProtectedDivisionFunctionGenerator()]
    terminals = [EphemeralRandomConstantGenerator(), InputVariableGenerator('x[0]')]
    sgp = SimpleGeneticProgramming(n_population=100, trees_depth=3, function_set=functions, terminal_set=terminals,
                                   problem_function=SimplePolynomialFromBook(), reproduction_probability=0.02,
                                   mutation_probability=0.08, crossover_probability=0.9)
    sgp.train()


if __name__ == '__main__':
    run_genetic_programming()

