from queue import PriorityQueue

from board import Board
from node import Node


class UniformCost:

    @staticmethod
    def search(start: Board, target: Board):

        queue: PriorityQueue[Node] = PriorityQueue()
        queue.put(Node(start))

        visited: list[list[list[int]]] = [start.get_array()]
        iteration: int = 0

        while not queue.empty():

            iteration += 1
            if iteration % 1_000 == 0:
                print(f"{iteration}th Iteration")

            current_node: Node = queue.get()
            current_board: Board = current_node.get_board()

            next_moves: list[tuple[int, int]] = current_board.get_next_moves()
            next_move: tuple[int, int]

            for next_move in next_moves:

                new_board: Board = current_board.move(next_move)
                if new_board.get_array() not in visited:

                    depth = current_node.get_depth() + 1
                    new_node = Node(new_board, depth=depth, parent=current_node)

                    if new_board == target:
                        return new_node

                    queue.put(new_node)
                    visited.append(new_board.get_array())
