''' Example of a random AI. The class name has to be the same as the module name.
'''

from __future__ import annotations
from copy import deepcopy # postpones the evaluation of the type hints, hence they do not need to be imported
import random
from othello import OthelloGame
import sys


class ThePension:
    '''The name of this class must be the same as its file.
    
    '''

    def __init__(self):
        pass

    def __str__(self):
        return "ThePension"

    def next_move(self, game : OthelloGame) -> tuple[int, int]:
        """Returns the next move to play.

        Args:
            board (othello.OthelloGame): _description_

        Returns:
            tuple[int, int]: the next move (for instance: (2, 3) for (row, column), starting from 0)
        """

        eval, move = self.minimax(State(game), 4, 1)

        return move


        return random.choice(legal_moves)

    def minimax(self, root : State, depth : int, minOrMax : int) -> tuple[int, tuple[int, int]]:
        if depth == 0 or root.final():
            return root.eval(), None

        optVal = minOrMax * -1000000
        optOp = None

        for op in root.ops():
            new = root.apply(op)

            val, dummy = self.minimax(new, depth - 1, -minOrMax)

            if val * minOrMax > optVal * minOrMax:
                optVal = val
                optOp = op

        return optVal, optOp


class State:
    def __init__(self, game : OthelloGame):
        self.game = game

    def eval(self) -> int:
        return self.game.get_scores()[0]

    def final(self):
        return self.game.is_game_over()
    
    # Return a list boards with every legal move applied to the current board
    def ops(self) -> list[tuple[int, int]]:# -> list[list[list[str]]]:
        return self.game.get_possible_move()


        # ops : list[list[list[str]]] = []

        # legal_moves = self.game.get_possible_move()

        # for legal_move in legal_moves:
        #     row, col = legal_move

        #     print("Current legal move" + str(legal_move))

        #     ops.append(self.game.move(row, col, True))
        #     self.game.switch_turn()

        # return ops

    def apply(self, op : list[list[str]]) -> ThePension:
        new_game = self.game.copy_game() # deepcopy(self.game)

        row, col = op

        new_game.move(row, col, False)

        return State(new_game)


    

