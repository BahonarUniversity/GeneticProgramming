from abc import ABC, abstractmethod

from TreeUtilities import TreeNode, Arguments, TwoArguments


class Functions(TreeNode):
    def get_value(self, arguments: Arguments):
        pass


class AdditionFunction(Functions):
    def get_value(self, arguments: TwoArguments):
        pass
        #return arguments.Argument1