import itertools
from typing import Self

import numpy as np


class Board:
    def __init__(self, *, dimension: int = 0, array: list[list[int]] = None):
        if dimension != 0:
            self.__dimension: int = dimension
            self.__array: np.ndarray = self.__initialize_board()
        else:
            self.__dimension: int = len(array)
            self.__array: np.ndarray = array

        self.__empty_position: tuple[int, int] = self.__get_position_of_empty()

    def get_array(self) -> list[list[int]]:
        return self.__array.tolist()

    # H score is the number of misplaced tiles
    def calculate_h_score(self, target: Self) -> int:
        row: int
        col: int

        h: int = 0
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                tile = self.__array[row][col]
                row_info, col_info = np.where(target.__array == tile)
                new_row = row_info[0]
                new_col = col_info[0]

                h += abs(row - new_row) + abs(col - new_col)

        return h

    def move(self, index: tuple[int, int]) -> Self:
        array: list[list[int]] = self.__array.copy()

        row: int
        col: int
        row, col = self.__get_position_of_empty()

        new_row: int
        new_col: int
        new_row, new_col = index

        array[row][col], array[new_row][new_col] = array[new_row][new_col], array[row][col]

        self.__empty_position = new_row, new_col

        return Board(array=array)

    def get_next_moves(self) -> list[tuple[int, int]]:
        valid_positions: list[tuple[int, int]] = []

        row: int
        col: int
        row, col = self.__get_position_of_empty()

        possible_positions: list[tuple[int, int]] = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]

        pos: tuple[int, int]
        for pos in possible_positions:
            next_row: int
            next_col: int
            next_row, next_col = pos

            if 0 <= next_row <= self.__dimension - 1 and 0 <= next_col <= self.__dimension - 1:
                valid_positions.append((next_row, next_col))

        return valid_positions

    def copy(self):
        return Board(array=self.__array.copy())

    def __initialize_board(self) -> list[list[int]]:
        board = np.array(list(range(self.__dimension ** 2)))
        solvable: bool = False

        while not solvable:
            np.random.shuffle(board)
            board = board.reshape((self.__dimension, self.__dimension))
            solvable = self.__is_solvable(board.tolist())

        return board

    def __is_solvable(self, array: list[list[int]]) -> bool:
        inversion_count: int = self.__get_inversion_count(array)
        empty_position: int = self.__find_empty_position(array)

        if self.__dimension % 2 != 0 and inversion_count % 2 == 0:
            return True

        if self.__dimension % 2 == 0:

            if inversion_count % 2 == 0 and empty_position % 2 != 0:
                return True

            if inversion_count % 2 != 0 and empty_position % 2 == 0:
                return True

        return False

    def __get_inversion_count(self, array: list[list[int]]) -> int:
        arr1: list[int] = []
        for y in array:
            arr1.extend(iter(y))

        array = arr1
        inv_count = 0
        for i in range(self.__dimension * self.__dimension - 1):
            for j in range(i + 1, self.__dimension * self.__dimension):
                if array[j] and array[i] and array[i] > array[j]:
                    inv_count += 1

        return inv_count

    def __find_empty_position(self, array: list[list[int]]) -> int:
        for row, col in itertools.product(range(self.__dimension - 1, -1, -1), range(self.__dimension - 1, -1, -1)):
            if array[row][col] == 0:
                return self.__dimension - row

    def __get_position_of_empty(self) -> tuple[int, int]:
        row_info, col_info = np.where(self.__array == 0)
        return row_info[0], col_info[0]

    def __eq__(self, other: Self):
        return np.array_equal(self.__array, other.__array)

    def __str__(self):
        return f"{self.__array}"
