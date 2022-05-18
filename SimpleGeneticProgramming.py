from typing import List

import np as np

from GPTree.Generator import TerminalGenerator, FunctionGenerator
from GPTree.TreeGenerator import RampedHalfAndHalfGenerator
from GPTree.TreeUtilities import TreeNode


class SimpleGeneticProgramming:

    def __init__(self, n_population: int, trees_depth: int,  terminal_set: List[TerminalGenerator],
                 function_set: List[FunctionGenerator]):
        self.n_population = n_population
        self.trees_depth = trees_depth

        self.tree_generator = RampedHalfAndHalfGenerator(terminal_set, function_set, self.trees_depth)
        self.programs: List[TreeNode] = self.generate_population()

        self.fitness = np.ones((n_population, ))

    def generate_population(self) -> List[TreeNode]:
        programs = []
        for i in range(self.n_population):
            programs.append(self.tree_generator.generate_tree())
        return programs

    def train(self):
        print('a')

    def evaluate(self):
        print('a')
