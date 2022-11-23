from queue import PriorityQueue

from board import Board
from node import Node


class Greedy:

    @staticmethod
    def search(start: Board, target: Board):

        ret: Node = None
        iteration = 0
        while ret is None:
            iteration += 1
            ret = Greedy.solve(start, target)

            if iteration % 100 == 0:
                print("Couldn't solve the problem. Trying again.")

        return ret

    @staticmethod
    def solve(start: Board, target: Board):

        h_score: int = start.calculate_h_score(target)

        if start == target:
            return Node(start, h_score=h_score)

        queue: PriorityQueue[Node] = PriorityQueue()
        queue.put(Node(start, h_score=h_score))

        visited: list[list[list[int]]] = [start.get_array()]
        min_current_board = None

        while not queue.empty():

            min_h_score: float = float("inf")

            current_node: Node = queue.get()
            current_board: Board = current_node.get_board()

            next_moves: list[tuple[int, int]] = current_board.get_next_moves()
            next_move: tuple[int, int]

            for next_move in next_moves:

                new_board: Board = current_board.move(next_move)
                if new_board.get_array() not in visited:

                    h_score: int = new_board.calculate_h_score(target)

                    if h_score < min_h_score:
                        min_h_score = h_score
                        min_current_board = new_board

                    if min_current_board == target:
                        return Node(min_current_board, h_score=min_h_score, parent=current_node)

            if min_h_score == float("inf"):
                return None

            new_node = Node(min_current_board, h_score=min_h_score, parent=current_node)
            queue.put(new_node)

            visited.append(min_current_board.get_array())
