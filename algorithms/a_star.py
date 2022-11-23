from queue import PriorityQueue

from board import Board
from node import Node


class AStar:

    @staticmethod
    def search(start: Board, target: Board):
        h_score: int = start.calculate_h_score(target)

        queue: PriorityQueue[Node] = PriorityQueue()
        queue.put(Node(start, h_score=h_score))

        visited: list[list[list[int]]] = [start.get_array()]
        iteration: int = 0

        while not queue.empty():

            iteration += 1
            if iteration % 1_000 == 0:
                print(f"{iteration}th Iteration")

            current_node: Node = queue.get()
            current_board: Board = current_node.get_board()
            current_g_score = current_node.get_depth()

            next_moves: list[tuple[int, int]] = current_board.get_next_moves()
            new_move: tuple[int, int]

            for new_move in next_moves:

                new_board: Board = current_board.move(new_move)
                if new_board.get_array() not in visited:

                    g_score: int = current_g_score + 1
                    h_score: int = new_board.calculate_h_score(target)

                    new_node: Node = Node(new_board, depth=g_score, h_score=h_score, parent=current_node)

                    if new_board == target:
                        return new_node

                    queue.put(new_node)
                    visited.append(new_board.get_array())
