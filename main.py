# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from Functions import AdditionFunction, SubtractionFunction, MultiplicationFunction, ProtectedDivisionFunction
from Terminals import IndependentVariable, EphemeralRandomConstant
from TreeGenerator import RampedHalfAndHalfGenerator

if __name__ == '__main__':
    functions = [AdditionFunction(), SubtractionFunction(), MultiplicationFunction(), ProtectedDivisionFunction()]
    terminals = [EphemeralRandomConstant(), IndependentVariable()]
    tg = RampedHalfAndHalfGenerator(terminals, functions, 2)
    tree = tg.generate_tree()
    print(tree)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
