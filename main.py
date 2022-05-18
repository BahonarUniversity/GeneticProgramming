# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from FunctionGenerator import AdditionFunctionGenerator, SubtractionFunctionGenerator, MultiplicationFunctionGenerator, \
    ProtectedDivisionFunctionGenerator
from TerminalGenerator import EphemeralRandomConstantGenerator, IndependentVariableGenerator
from TreeGenerator import RampedHalfAndHalfGenerator

if __name__ == '__main__':
    functions = [AdditionFunctionGenerator(), SubtractionFunctionGenerator(), MultiplicationFunctionGenerator(),
                 ProtectedDivisionFunctionGenerator()]
    terminals = [EphemeralRandomConstantGenerator(), IndependentVariableGenerator()]
    tg = RampedHalfAndHalfGenerator(terminals, functions, 2)
    tree = tg.generate_tree()
    print(tree)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
