from queue import LifoQueue

from board import Board
from node import Node


class LimitedDepth:

    @staticmethod
    def search(start: Board, target: Board, *, limit_depth: int = 100_000):

        stack: LifoQueue[Node] = LifoQueue()
        stack.put(Node(start))

        visited: list[list[list[int]]] = [start.get_array()]
        iteration = 0

        while not stack.empty():

            iteration += 1
            if iteration % 1_000 == 0:
                print(f"{iteration}th Iteration")

            current_node: Node = stack.get()
            current_board: Board = current_node.get_board()

            current_depth: int = current_node.get_depth()

            if current_depth > limit_depth:
                return None

            next_moves: list[tuple[int, int]] = current_board.get_next_moves()
            next_move: tuple[int, int]

            for next_move in next_moves:

                new_board = current_board.move(next_move)
                if new_board.get_array() not in visited:
                    new_node: Node = Node(new_board, depth=current_node.get_depth() + 1, parent=current_node)

                    if new_board == target:
                        return new_node

                    stack.put(new_node)
                    visited.append(new_board.get_array())
