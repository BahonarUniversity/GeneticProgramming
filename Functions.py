from abc import ABC
from typing import List

from TreeUtilities import TreeNode, FunctionNode


class BinaryTreeNode(FunctionNode, ABC):

    def __init__(self):
        super().__init__()
        self.sub_nodes_count: int = 2

    def add_sub_nodes(self, sub_nodes: List[TreeNode]):
        self.sub_nodes = []
        self.sub_nodes.append(sub_nodes[0])
        self.sub_nodes.append(sub_nodes[1])


class TernaryTreeNode(FunctionNode, ABC):

    def __init__(self):
        super().__init__()
        self.sub_nodes_count: int = 3

    def add_sub_nodes(self, sub_nodes: List[TreeNode]):
        self.sub_nodes = []
        self.sub_nodes.append(sub_nodes[0])
        self.sub_nodes.append(sub_nodes[1])
        self.sub_nodes.append(sub_nodes[2])


###############################################################


class AdditionFunction(BinaryTreeNode):
    def get_value(self):
        return self.sub_node_1.get_value() + self.sub_node_2.get_value()


class SubtractionFunction(BinaryTreeNode):
    def get_value(self):
        return self.sub_node_1.get_value() - self.sub_node_2.get_value()


class MultiplicationFunction(BinaryTreeNode):
    def get_value(self):
        return self.sub_node_1.get_value() * self.sub_node_2.get_value()


class ProtectedDivisionFunction(BinaryTreeNode):
    def get_value(self):
        return self.sub_node_1.get_value() / self.sub_node_2.get_value() if self.sub_node_2 != 0 else 0
