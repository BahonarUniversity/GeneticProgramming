# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from GPTree.FunctionGenerator import AdditionFunctionGenerator, SubtractionFunctionGenerator, MultiplicationFunctionGenerator, \
    ProtectedDivisionFunctionGenerator
from SimpleGeneticProgramming import SimpleGeneticProgramming
from GPTree.TerminalGenerator import EphemeralRandomConstantGenerator, InputVariableGenerator

# Press the green button in the gutter to run the script.


def run_genetic_programming():
    functions = [AdditionFunctionGenerator(), SubtractionFunctionGenerator(), MultiplicationFunctionGenerator(),
                 ProtectedDivisionFunctionGenerator()]
    terminals = [EphemeralRandomConstantGenerator(), InputVariableGenerator('x')]
    sgp = SimpleGeneticProgramming(n_population=4, trees_depth=2, function_set=functions, terminal_set=functions)
    sgp.train()
    composition = tree.get_composition()


if __name__ == '__main__':
    run_genetic_programming()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
