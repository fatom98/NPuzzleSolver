from typing import Self

from board import Board


class Node:
    def __init__(self, board: Board, *, depth: int = 0, h_score: float = 0, parent: Self = None):
        self.__board: Board = board
        self.__depth: int = depth
        self.__h_score: float = h_score
        self.__f_score: float = self.__set_f_score()
        self.__parent: Self = parent

    def get_board(self) -> Board:
        return self.__board.copy()

    def get_f_score(self) -> float:
        return self.__f_score

    def get_depth(self) -> int:
        return self.__depth

    def get_h_score(self) -> float:
        return self.__h_score

    def get_parent(self) -> Self:
        return self.__parent

    def __set_f_score(self):
        return self.__depth + self.__h_score

    def __eq__(self, other: Self) -> bool:
        return self.__board == other.get_board() and self.__f_score == other.get_f_score()

    def __lt__(self, other: Self):
        if self.__f_score == other.get_f_score():
            return self.__h_score < other.get_h_score()

        return self.__f_score < other.get_f_score()
