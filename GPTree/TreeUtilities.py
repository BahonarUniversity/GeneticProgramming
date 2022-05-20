from abc import ABC, abstractmethod
from typing import List


class TreeNode(ABC):
    __nodes: [] = None
    @abstractmethod
    def get_composition(self):
        pass

    @abstractmethod
    def __take_all_nodes(self):
        pass

    def select_random_node(self):
        if self.__nodes is None:
            self.__nodes = self.__take_all_nodes()


class TerminalNode(TreeNode, ABC):

    def __take_all_nodes(self):
        self.__nodes = []
        self.__nodes.append(self)


class FunctionNode(TreeNode, ABC):

    def __init__(self):
        self.sub_nodes_count: int = 0
        self.sub_nodes: List[TreeNode] = []

    @abstractmethod
    def add_sub_nodes(self, sub_nodes: List[TreeNode]):
        pass

    def __take_all_nodes(self):
        self.__nodes = []
        self.__nodes.append(self)
        # take subnodes



