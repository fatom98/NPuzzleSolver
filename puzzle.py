import time
from typing import Callable

from algorithm_type import AlgorithmType
from algorithms.a_star import AStar
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.greedy import Greedy
from algorithms.iterative_depth import IDS
from algorithms.limited_depth import LimitedDepth
from algorithms.uniform_cost import UniformCost
from board import Board
from node import Node


def decorator(function: Callable):
    def wrapped_function(self):
        start = time.time()
        last_node = function(self)
        end = time.time()
        duration = end - start

        Puzzle.calculate_result(self, last_node, duration)

    return wrapped_function


class Puzzle:
    def __init__(self, *, dimension: int):
        self.__start: Board = Board(dimension=dimension)
        self.__end: Board = Board(dimension=dimension)

        self.__algorithm_name: str = ""
        self.__dimension: int = dimension

        print(f"Start \n{self.__start}\n")
        print(f"Target \n{self.__end}\n")
        print("-" * 20)

    def solve(self, *, algorithm_type: AlgorithmType) -> None:
        match algorithm_type:
            case AlgorithmType.A_STAR:
                self.__solve_with_a_star()
            case AlgorithmType.BREADTH_FIRST_SEARCH:
                self.__solve_with_bfs()
            case AlgorithmType.DEPTH_FIRST_SEARCH:
                self.__solve_with_dfs()
            case AlgorithmType.GREEDY:
                self.__solve_with_greedy()
            case AlgorithmType.ITERATIVE_DEPTH:
                self.__solve_with_ids()
            case AlgorithmType.UNIFORM_COST_SEARCH:
                self.__solve_with_u_cost()
            case AlgorithmType.LIMITED_DEPTH:
                self.__solve_with_limited_depth()
            case _:
                raise ValueError("Invalid Algorithm Type")

    @decorator
    def __solve_with_a_star(self) -> Node:
        print("Solving puzzle with A* Algorithm\n")
        self.__algorithm_name = AlgorithmType.A_STAR.name
        return AStar.search(self.__start, self.__end)

    @decorator
    def __solve_with_bfs(self) -> Node:
        print("Solving puzzle with BFS Algorithm\n")
        self.__algorithm_name = AlgorithmType.BREADTH_FIRST_SEARCH.name
        return BFS.search(self.__start, self.__end)

    @decorator
    def __solve_with_dfs(self) -> Node:
        print("Solving puzzle with DFS Algorithm\n")
        self.__algorithm_name = AlgorithmType.DEPTH_FIRST_SEARCH.name
        return DFS.search(self.__start, self.__end)

    @decorator
    def __solve_with_greedy(self) -> Node:
        print("Solving puzzle with Greedy Algorithm\n")
        self.__algorithm_name = AlgorithmType.GREEDY.name
        return Greedy.search(self.__start, self.__end)

    @decorator
    def __solve_with_ids(self) -> Node:
        print("Solving puzzle with IDS Algorithm\n")
        self.__algorithm_name = AlgorithmType.ITERATIVE_DEPTH.name
        return IDS.search(self.__start, self.__end)

    @decorator
    def __solve_with_u_cost(self) -> Node:
        print("Solving puzzle with Uniform Cost Algorithm\n")
        self.__algorithm_name = AlgorithmType.UNIFORM_COST_SEARCH.name
        return UniformCost.search(self.__start, self.__end)

    @decorator
    def __solve_with_limited_depth(self) -> Node:
        print("Solving puzzle with Limited Depth Cost Algorithm\n")
        self.__algorithm_name = AlgorithmType.LIMITED_DEPTH.name
        return LimitedDepth.search(self.__start, self.__end)

    def calculate_result(self, last_node: Node, duration: float):

        if last_node is None:
            print("Puzzle could not be solved :(")
            return

        print("\nPuzzle is solved :)")

        history: list[Board] = [last_node.get_board()]
        parent = last_node

        while True:
            parent = parent.get_parent()

            if parent is None:
                break

            history.append(parent.get_board())

        self.__write_history_to_file(history, duration)

    def __write_history_to_file(self, history: list[Board], duration: float):
        execution_time_string: str = f"Execution time is: {duration: .2f}s.\n"
        step_count_string: str = f"It took {len(history)} steps to reach to target.\n"

        with open(f"outputs/{self.__algorithm_name}_{self.__dimension}N.md", "w+") as file:

            file.write(execution_time_string)
            file.write("\n")
            file.write(step_count_string)
            file.write("\n\n\n")

            for index, board in enumerate(history[::-1]):

                printed = False
                for row in board.get_array():
                    file.write("|")
                    for element in row:
                        file.write(f"{element}|")
                    file.write("\n")

                    if not printed:
                        file.write("|")

                        for _ in range(self.__dimension):
                            file.write("---|")

                        file.write("\n")
                        printed = True

                if index != len(history) - 1:
                    file.write("----------&darr;----------")
                    file.write("\n\n")
