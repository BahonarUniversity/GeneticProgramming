from abc import ABC, abstractmethod


class Arguments(ABC):
    pass


class TwoArguments(Arguments):
    Argument1 = 0.0
    Argument2 = 0.0


class ThreeArguments(Arguments):
    Argument1 = 0.0
    Argument2 = 0.0
    Argument3 = 0.0


class TreeNode(ABC):
    @abstractmethod
    def get_value(self, arguments: Arguments):
        pass


class TerminalNode(TreeNode, ABC):
    pass


class BinaryTreeNode(TreeNode, ABC):
    sub_node_1: TreeNode = None
    sub_node_2: TreeNode = None


class TernaryTreeNode(TreeNode, ABC):
    sub_node_1: TreeNode = None
    sub_node_2: TreeNode = None
    sub_node_3: TreeNode = None


