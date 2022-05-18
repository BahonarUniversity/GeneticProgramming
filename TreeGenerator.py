import copy
import random
from abc import ABC, abstractmethod
from typing import List

from TreeUtilities import TerminalNode, FunctionNode, TreeNode


class TreeGenerator(ABC):
    def __init__(self, terminal_set: List[TerminalNode], function_set: List[FunctionNode]):
        self.terminal_set = terminal_set
        self.function_set = function_set

    @abstractmethod
    def generate_tree(self):
        pass


class FullTreeGenerator(TreeGenerator):
    def __init__(self, terminal_set: List[TerminalNode], function_set: List[FunctionNode], max_depth: int):
        super().__init__(terminal_set, function_set)
        self.max_depth = max_depth
        self.__function_count = len(function_set)
        self.__terminal_count = len(terminal_set)

    def generate_tree(self):
        return self.__generate_node()

    def __generate_node(self, depth: int = 0) -> TreeNode:
        if depth == self.max_depth:
            random_terminal_index = random.Random().randint(0, self.__terminal_count-1)
            random_terminal = self.terminal_set[random_terminal_index]
            new_node = copy.deepcopy(random_terminal)
        else:
            random_function_index = random.Random().randint(0, self.__function_count-1)
            random_function = self.function_set[random_function_index]
            new_node = copy.deepcopy(random_function)
            sub_nodes: List[TreeNode] = [None]
            for i in range(new_node.sub_nodes_count):
                sub_nodes.append(self.__generate_node(depth + 1))
            new_node.add_sub_nodes(sub_nodes)
        return new_node


class GrowTreeGenerator(TreeGenerator):
    def __init__(self, terminal_set: List[TerminalNode], function_set: List[FunctionNode], max_depth: int):
        super().__init__(terminal_set, function_set)
        self.max_depth = max_depth
        self.__function_count = len(function_set)
        self.__terminal_count = len(terminal_set)

    def generate_tree(self):
        return self.__generate_node()

    def __generate_node(self, depth: int = 0) -> TreeNode:
        if depth == self.max_depth:
            new_node = self.__add_terminal_node()
        else:
            if random.Random().random() > 0.5:
                new_node = self.__add_function_node()
                sub_nodes: List[TreeNode] = [None]
                for i in range(new_node.sub_nodes_count):
                    sub_nodes.append(self.__generate_node(depth + 1))
                new_node.add_sub_nodes(sub_nodes)
            else:
                new_node = self.__add_terminal_node()
        return new_node

    def __add_terminal_node(self):
        random_terminal_index = random.Random().randint(0, self.__terminal_count-1)
        random_terminal = self.terminal_set[random_terminal_index]
        return copy.deepcopy(random_terminal)

    def __add_function_node(self):
        random_function_index = random.Random().randint(0, self.__function_count-1)
        random_function = self.function_set[random_function_index]
        return copy.deepcopy(random_function)
