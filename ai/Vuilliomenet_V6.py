'''
Example of a random AI. The class name has to be the same as the module name.
'''

from __future__ import annotations
from othello import OthelloGame

class Vuilliomenet_V6:
    '''
    The name of this class must be the same as its file.
    '''

    def __init__(self):
        pass

    def __str__(self):
        return "Vuilliomenet_V5"

    def next_move(self, game : OthelloGame) -> tuple[int, int]:
        """Returns the next move to play.

        Args:
            board (othello.OthelloGame): _description_

        Returns:
            tuple[int, int]: the next move (for instance: (2, 3) for (row, column), starting from 0)
        """

        eval, move = self.alphabeta(State(game), 4, 1, float('inf'))

        return move

    def alphabeta(self, root : State, depth : int, minOrMax : int, parentValue : int) -> tuple[int, tuple[int, int]]:
        if depth == 0 or root.final():
            return root.eval(), None

        optVal = minOrMax * float('-inf')
        optOp = None

        for op in root.ops():
            new = root.apply(op)

            val, dummy = self.alphabeta(new, depth - 1, -minOrMax, optVal)

            if val * minOrMax > optVal * minOrMax:
                optVal = val
                optOp = op

                if optVal * minOrMax > parentValue * minOrMax:
                    break

        return optVal, optOp


class State:
    def __init__(self, game : OthelloGame):
        self.game = game

    def eval(self) -> int:
        return get_position_score(self.game.get_board(), self.game.get_turn())

    def final(self):
        return self.game.is_game_over()
    
    def ops(self) -> list[tuple[int, int]]:
        return self.game.get_possible_move()

    def apply(self, op : tuple[int, int]) -> Vuilliomenet_V6:
        new_game = self.game.copy_game()

        row, col = op

        new_game.move(row, col, False)

        return State(new_game)

# The total is 100
# 0 pts for the border of the corner
# 50% of the points are just for the corners
# 25% of the points are for the 3x3 center square
# 15% of the points are for the borders
# 10% of the points are for the rest
score_array_1 = [
    [12.5, 0, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0, 12.5],
    [0, 0, 0.45, 0.45, 0.45, 0.45, 0.45, 0, 0],
    [0.9375, 0.45, 0.45, 2.78, 2.78, 2.78, 0.45, 0.45, 0.9375],
    [0.9375, 0.45, 0.45, 2.78, 2.78, 2.78, 0.45, 0.45, 0.9375],
    [0.9375, 0.45, 0.45, 2.78, 2.78, 2.78, 0.45, 0.45, 0.9375],
    [0, 0, 0.45, 0.45, 0.45, 0.45, 0.45, 0, 0],
    [12.5, 0, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0, 12.5]
    ]

# The total is 100
# 0 pts for the border of the corner
# 50% of the points are just for the corners
# 15% of the points are for the 3x3 center square
# 25% of the points are for the borders
# 10% of the points are for the rest
score_array_2 = [
    [12.5, 0, 1.563, 1.563, 1.563, 1.563, 1.563, 0, 12.5],
    [0, 0, 0.45, 0.45, 0.45, 0.45, 0.45, 0, 0],
    [1.563, 0.45, 0.45, 1.67, 1.67, 1.67, 0.45, 0.45, 1.563],
    [1.563, 0.45, 0.45, 1.67, 1.67, 1.67, 0.45, 0.45, 1.563],
    [1.563, 0.45, 0.45, 1.67, 1.67, 1.67, 0.45, 0.45, 1.563],
    [0, 0, 0.45, 0.45, 0.45, 0.45, 0.45, 0, 0],
    [12.5, 0, 1.563, 1.563, 1.563, 1.563, 1.563, 0, 12.5]
    ]

# The total is 100
# 0 pts for the border of the corner
# 50% of the points are just for the corners
# 20% of the points are for the 3x3 center square
# 25% of the points are for the borders
# 5% of the points are for the rest
score_array_3 = [
    [12.5, 0, 1.563, 1.563, 1.563, 1.563, 1.563, 0, 12.5],
    [0, 0, 0.23, 0.23, 0.23, 0.23, 0.23, 0, 0],
    [1.563, 0.23, 0.23, 2.23, 2.23, 2.23, 0.23, 0.23, 1.563],
    [1.563, 0.23, 0.23, 2.23, 2.23, 2.23, 0.23, 0.23, 1.563],
    [1.563, 0.23, 0.23, 2.23, 2.23, 2.23, 0.23, 0.23, 1.563],
    [0, 0, 0.23, 0.23, 0.23, 0.23, 0.23, 0, 0],
    [12.5, 0, 1.563, 1.563, 1.563, 1.563, 1.563, 0, 12.5]
    ]

def get_position_score(board : list[list[str]], color : str) -> int:
    score = 0

    w = len(board)
    h = len(board[0])

    for xi in range(0, w):
        for yi in range(0, h):
            if board[xi][yi] == color:
                score += score_array_2[xi][yi]

    return score