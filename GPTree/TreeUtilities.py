import random
from abc import ABC, abstractmethod
from typing import List


class TreeNode(ABC):
    def __init__(self):
        self.nodes: [] = None
        self.parent = None

    @abstractmethod
    def get_composition(self):
        pass

    @abstractmethod
    def _take_all_nodes(self):
        pass

    def select_random_node(self):
        self._take_all_nodes()
        rand = random.Random().randint(1, (len(self.nodes) - 1))
        return self.nodes[rand]


class TerminalNode(TreeNode, ABC):

    def _take_all_nodes(self):
        self.nodes = []
        self.nodes.append(self)


class FunctionNode(TreeNode, ABC):

    def __init__(self):
        super().__init__()
        self.sub_nodes_count: int = 0
        self.sub_nodes: List[TreeNode] = []

    @abstractmethod
    def add_sub_nodes(self, sub_nodes: List[TreeNode]):
        pass

    def _take_all_nodes(self):
        self.nodes = []
        self.nodes.append(self)
        self.__take_sub_nodes(self)

    def __take_sub_nodes(self, function_node):
        for i in range(len(function_node.sub_nodes)):
            self.nodes.append(function_node.sub_nodes[i])
            if function_node.sub_nodes[i] is type(FunctionNode):
                self.__take_sub_nodes(function_node.sub_nodes[i])
