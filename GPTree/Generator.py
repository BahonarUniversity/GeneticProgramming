from abc import ABC, abstractmethod

from GPTree.TreeUtilities import FunctionNode, TerminalNode


class Generator(ABC):
    @abstractmethod
    def generate(self):
        pass


class FunctionGenerator(ABC):
    @abstractmethod
    def generate(self) -> FunctionNode:
        pass


class TerminalGenerator(ABC):
    @abstractmethod
    def generate(self) -> TerminalNode:
        pass
