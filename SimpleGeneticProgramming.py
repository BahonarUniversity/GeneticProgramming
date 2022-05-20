import random
import sys
from typing import List, Tuple

import numpy as np
import pandas as pd

from GPTree.Generator import TerminalGenerator, FunctionGenerator
from GPTree.TreeGenerator import RampedHalfAndHalfGenerator
from GPTree.TreeUtilities import TreeNode
from ProblemFunction import ProblemFunction


class SimpleGeneticProgramming:

    def __init__(self, n_population: int, trees_depth: int, terminal_set: List[TerminalGenerator],
                 function_set: List[FunctionGenerator], problem_function: ProblemFunction,
                 target_input_range: List[Tuple[float, float]] = List[(-2, 2)], evaluation_step: float = 0.1,
                 reproduction_probability: float = 0.08, mutation_probability: float = 0.02,
                 crossover_probability: float = 0.9):
        self.n_population = n_population
        self.trees_depth = trees_depth
        self.input_data, self.output_data = problem_function.generate_data(target_input_range, evaluation_step)
        self.target_input_range = target_input_range
        self.evaluation_step = evaluation_step

        self.tree_generator = RampedHalfAndHalfGenerator(terminal_set, function_set, self.trees_depth)
        self._lambda_prefix = self.setup_function_lambda()
        self.programs: List[TreeNode] = self.generate_population()
        self.fitness, self.probabilities, self.accumulated_probabilities = self.evaluate()
        self.reproduction_probability = reproduction_probability
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability

    def generate_population(self) -> List[TreeNode]:
        programs = []
        for i in range(self.n_population):
            programs.append(self.tree_generator.generate_tree())
        return programs

    def train(self, input_data: pd.DataFrame, output_data: pd.DataFrame):
        while min(self.fitness) > 0.1:
            rand = random.Random.uniform()
            children: List[TreeNode] = []
            for i in range(self.n_population):
                if rand < self.reproduction_probability:
                    children.append(self.__tournament_selection())
                elif rand < self.reproduction_probability + self.mutation_probability:
                    children.append(self.__mutation(self.__tournament_selection()))
                elif rand < self.reproduction_probability + self.mutation_probability + self.crossover_probability:
                    children.append(self.__crossover(self.__tournament_selection(), self.__tournament_selection()))

            self.programs = children
            self.fitness, self.probabilities, self.accumulated_probabilities = self.evaluate()

    def __mutation(self, program: TreeNode):
        program.select_random_node()
        return program

    def __crossover(self, program_1: TreeNode, program_2: TreeNode):
        return program_1

    def __select_random_program(self):
        rand = random.Random.uniform()
        for i in range(self.n_population):
            if rand < self.accumulated_probabilities[i]:
                return self.programs[i]

    def __tournament_selection(self):
        best_selection = random.Random.randint(0, self.n_population-1)
        for i in range(4):
            next_selection = random.Random.randint(0, self.n_population-1)
            if self.fitness[next_selection] < self.fitness[best_selection]:
                best_selection = next_selection
        return self.programs[best_selection]


    def setup_function_lambda(self):
        variables_count = self.problem_function.get_variables_count()
        return f'genetic_function = lambda x: []: '

    def evaluate(self):
        fitness = np.ones((self.n_population, ))
        for i in range(self.n_population):
            lambda_str = f'{self._lambda_prefix}{self.n_population[i].get_composition()}'
            lambda_exe = exec(lambda_str)
            integration = 0
            for j in range(self.input_data.shape[0]):
                output = lambda_exe(self.input_data.iloc[j])
                integration += abs(self.output_data.iloc[j] - output)
            fitness[i] = integration / self.input_data.shape[0]

        probabilities = 1 / fitness
        sum_fitness = sum(probabilities)
        probabilities = probabilities / sum_fitness
        accumulated_probabilities = np.cumsum(probabilities)

        return fitness, probabilities, accumulated_probabilities

