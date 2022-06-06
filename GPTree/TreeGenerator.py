import random
from abc import ABC, abstractmethod
from typing import List

from GPTree.Generator import TerminalGenerator, FunctionGenerator
from GPTree.TreeUtilities import TreeNode


class TreeGenerator(ABC):
    def __init__(self, terminal_set: List[TerminalGenerator], function_set: List[FunctionGenerator]):
        self.terminal_set = terminal_set
        self.function_set = function_set
        self._function_count = len(function_set)
        self._terminal_count = len(terminal_set)

    @abstractmethod
    def generate_tree(self) -> TreeNode:
        pass

    def _add_terminal_node(self):
        random_terminal_index = random.Random().randint(0, self._terminal_count - 1)
        random_terminal = self.terminal_set[random_terminal_index]
        return random_terminal.generate()

    def _add_function_node(self, depth):
        random_function_index = random.Random().randint(0, self._function_count - 1)
        random_function = self.function_set[random_function_index]
        new_node = random_function.generate()
        sub_nodes: List[TreeNode] = []
        for i in range(new_node.sub_nodes_count):
            sub_node = self._generate_node(depth + 1)
            sub_node.parent = new_node
            sub_nodes.append(sub_node)
        new_node.add_sub_nodes(sub_nodes)
        return new_node

    @abstractmethod
    def _generate_node(self, depth: int = 0) -> TreeNode:
        pass


class FullTreeGenerator(TreeGenerator):
    def __init__(self, terminal_set: List[TerminalGenerator], function_set: List[FunctionGenerator], max_depth: int):
        super().__init__(terminal_set, function_set)
        self.max_depth = max_depth

    def generate_tree(self) -> TreeNode:
        return self._generate_node()

    def _generate_node(self, depth: int = 0) -> TreeNode:
        if depth == self.max_depth:
            new_node = self._add_terminal_node()
        else:
            new_node = self._add_function_node(depth)
        return new_node


class GrowTreeGenerator(TreeGenerator):
    def __init__(self, terminal_set: List[TerminalGenerator], function_set: List[FunctionGenerator], max_depth: int):
        super().__init__(terminal_set, function_set)
        self.max_depth = max_depth

    def generate_tree(self) -> TreeNode:
        return self._generate_node()

    def _generate_node(self, depth: int = 0) -> TreeNode:
        if depth == 0:
            new_node = self._add_function_node(depth)
        elif depth == self.max_depth:
            new_node = self._add_terminal_node()
        else:
            if random.Random().random() > 0.5:
                new_node = self._add_function_node(depth)
            else:
                new_node = self._add_terminal_node()
        return new_node


class RampedHalfAndHalfGenerator(TreeGenerator):

    def _generate_node(self, depth: int = 0) -> TreeNode:
        pass

    def __init__(self, terminal_set: List[TerminalGenerator], function_set: List[FunctionGenerator], max_depth: int):
        super().__init__(terminal_set, function_set)
        self.max_depth = max_depth
        self.__grow_generator: GrowTreeGenerator = GrowTreeGenerator(terminal_set, function_set, max_depth)
        self.__full_generator: FullTreeGenerator = FullTreeGenerator(terminal_set, function_set, max_depth)

    def generate_tree(self) -> TreeNode:
        rand = random.Random().random()
        new_node = self.__full_generator.generate_tree() if rand > 0.5 else self.__grow_generator.generate_tree()
        # sub_nodes: List[TreeNode] = []
        # for i in range(new_node.sub_nodes_count):
        #     if i % 2 == 0:
        #         sub_node = self.__full_generator.generate_tree()
        #     else:
        #         sub_node = self.__grow_generator.generate_tree()
        #     sub_node.parent = new_node
        #     sub_nodes.append(sub_node)
        # new_node.add_sub_nodes(sub_nodes)
        return new_node
