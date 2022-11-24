from algorithm_type import AlgorithmType
from puzzle import Puzzle


def main():
    dimension: int
    for dimension in [4, 5]:
        puzzle: Puzzle = Puzzle(dimension=dimension)

        puzzle.solve(algorithm_type=AlgorithmType.A_STAR)
        puzzle.solve(algorithm_type=AlgorithmType.BREADTH_FIRST_SEARCH)
        puzzle.solve(algorithm_type=AlgorithmType.DEPTH_FIRST_SEARCH)
        puzzle.solve(algorithm_type=AlgorithmType.GREEDY)
        puzzle.solve(algorithm_type=AlgorithmType.ITERATIVE_DEPTH)
        puzzle.solve(algorithm_type=AlgorithmType.LIMITED_DEPTH)
        puzzle.solve(algorithm_type=AlgorithmType.UNIFORM_COST_SEARCH)


if __name__ == '__main__':
    main()
