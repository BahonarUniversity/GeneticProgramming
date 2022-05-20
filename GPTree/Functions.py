from abc import ABC
from typing import List

from GPTree.TreeUtilities import TreeNode, FunctionNode


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
    def get_composition(self):
        return f'({self.sub_nodes[0].get_composition()} + {self.sub_nodes[1].get_composition()})'


class SubtractionFunction(BinaryTreeNode):
    def get_composition(self):
        return f'({self.sub_nodes[0].get_composition()} - {self.sub_nodes[1].get_composition()})'


class MultiplicationFunction(BinaryTreeNode):
    def get_composition(self):
        return f'({self.sub_nodes[0].get_composition()} * {self.sub_nodes[1].get_composition()})'


class ProtectedDivisionFunction(BinaryTreeNode):
    def get_composition(self):
        return f'({self.sub_nodes[0].get_composition()} / {self.sub_nodes[1].get_composition()})'\
            if self.sub_nodes[1] != 0 \
            else '%.4f' % 1
