import copy
import random
import sys
from typing import List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from GPTree.Generator import TerminalGenerator, FunctionGenerator
from GPTree.TreeGenerator import RampedHalfAndHalfGenerator
from GPTree.TreeUtilities import TreeNode
from ProblemFunction import ProblemFunction


class SimpleGeneticProgramming:

    def __init__(self, n_population: int, trees_depth: int, terminal_set: List[TerminalGenerator],
                 function_set: List[FunctionGenerator], problem_function: ProblemFunction,
                 target_input_range: List[Tuple[float, float]] = [(-1, 1)], evaluation_step: float = 0.1,
                 reproduction_probability: float = 0.08, mutation_probability: float = 0.02,
                 crossover_probability: float = 0.9, max_iteration: int = 100):
        self.n_population = n_population
        self.trees_depth = trees_depth
        self.problem_function = problem_function
        self.input_data, self.output_data = problem_function.generate_data(target_input_range, evaluation_step)
        self.target_input_range = target_input_range
        self.evaluation_step = evaluation_step
        self.max_iteration = max_iteration

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

    def train(self):
        iteration = 0
        fitnesses = np.zeros((self.max_iteration, self.n_population))
        while min(self.fitness) > 0.1 and iteration < self.max_iteration:
            children: List[TreeNode] = []
            for i in range(self.n_population):
                rand = np.random.uniform(0, 1.0)
                if rand < self.reproduction_probability:
                    children.append(self.__tournament_selection(4))
                elif rand < self.reproduction_probability + self.mutation_probability:
                    children.append(self.__mutation(self.__tournament_selection(3)))
                elif rand < self.reproduction_probability + self.mutation_probability + self.crossover_probability:
                    children.append(self.__crossover(self.__tournament_selection(2), self.__tournament_selection(2)))

            self.programs = children
            self.fitness, self.probabilities, self.accumulated_probabilities = self.evaluate()
            fitnesses[iteration] = self.fitness
            iteration += 1
            print("program:", self.programs[np.argmin(self.fitness)].get_composition())
            print(f"iter {iteration}: np.min = {np.min(self.fitness)}")
        self.plot_fitness(0, self.max_iteration, fitnesses)

    def plot_fitness(self, begin, end, fitness: np.ndarray):
        plt.plot(range(begin, end), np.mean(fitness[begin:, :], axis=1), label='average mean fitness')
        plt.plot(range(begin, end), np.min(fitness[begin:, :], axis=1), color='red', label='best so far')
        plt.xlabel('iteration')
        plt.ylabel('fitness value')
        plt.legend()
        plt.show()

    def __mutation(self, program: TreeNode):
        program_copy = copy.deepcopy(program)
        random_node: TreeNode = program_copy.select_random_node()
        random_program = self.tree_generator.generate_tree()
        random_node.parent.sub_nodes.remove(random_node)
        random_node.parent.sub_nodes.append(random_program)
        random_program.parent = random_node.parent
        return program_copy

    @staticmethod
    def __crossover(program_1: TreeNode, program_2: TreeNode):

        program_1_copy = copy.deepcopy(program_1)
        random_node1: TreeNode = program_1_copy.select_random_node()
        random_node2: TreeNode = copy.deepcopy(program_2.select_random_node())
        random_node1.parent.sub_nodes.remove(random_node1)
        random_node1.parent.sub_nodes.append(random_node2)
        random_node2.parent = random_node1.parent
        return program_1_copy

    def __select_random_program(self):
        rand = random.Random().uniform()
        for i in range(self.n_population):
            if rand < self.accumulated_probabilities[i]:
                return self.programs[i]

    def __tournament_selection(self, tournament_size=3):
        best_selection = random.Random().randint(0, self.n_population-1)
        for i in range(tournament_size):
            next_selection = random.Random().randint(0, self.n_population-1)
            if self.fitness[next_selection] < self.fitness[best_selection]:
                best_selection = next_selection
        return self.programs[best_selection]

    def setup_function_lambda(self):
        variables_count = self.problem_function.get_variables_count()
        return f'lambda x: ' # genetic_function =

    def evaluate(self):
        fitness = np.ones((self.n_population, ))
        for i in range(self.n_population):
            lambda_str = f'{self._lambda_prefix}{self.programs[i].get_composition()}'
            genetic_function = eval(lambda_str)
            integration = 0
            for j in range(self.input_data.shape[0]):
                output = genetic_function(self.input_data.iloc[j])
                integration += abs(self.output_data.iloc[j] - output)
            fitness[i] = integration / self.input_data.shape[0]

        probabilities = 1 / fitness
        sum_fitness = sum(probabilities)
        probabilities = probabilities / sum_fitness
        accumulated_probabilities = np.cumsum(probabilities)

        return fitness, probabilities, accumulated_probabilities

