from abc import ABC, abstractmethod
from typing import List


class TreeNode(ABC):
    @abstractmethod
    def get_composition(self):
        pass


class TerminalNode(TreeNode, ABC):
    pass


class FunctionNode(TreeNode, ABC):

    def __init__(self):
        self.sub_nodes_count: int = 0
        self.sub_nodes: List[TreeNode] = []

    @abstractmethod
    def add_sub_nodes(self, sub_nodes: List[TreeNode]):
        pass



