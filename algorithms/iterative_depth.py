from queue import LifoQueue

from board import Board
from node import Node


class IDS:

    @staticmethod
    def search(start: Board, target: Board, depth_limit: int = 10):
        ret: Node = None
        while ret is None:
            depth_limit *= 2
            ret = IDS.__solve(start, target, depth_limit)

            print(f"Couldn't solve the problem. Increasing the depth to {depth_limit}.")

        return ret

    @staticmethod
    def __solve(start: Board, target: Board, depth_limit: int):
        stack: LifoQueue[Node] = LifoQueue()
        stack.put(Node(start))

        visited: list[list[list[int]]] = [start.get_array()]

        while not stack.empty():

            current_node: Node = stack.get()
            current_board: Board = current_node.get_board()
            current_depth: int = current_node.get_depth()

            if current_depth > depth_limit:
                return None

            next_moves: list[tuple[int, int]] = current_board.get_next_moves()
            next_move: tuple[int, int]

            for next_move in next_moves:

                new_board: Board = current_board.move(next_move)
                if new_board.get_array() not in visited:
                    new_node: Node = Node(new_board, depth=current_node.get_depth() + 1, parent=current_node)

                    if new_board == target:
                        return new_node

                    stack.put(new_node)
                    visited.append(new_board.get_array())
