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

        eval, move = self.alphabeta(State(game), 5, 1, 0)

        return move

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

    def alphabeta(self, root : State, depth : int, minOrMax : int, parentValue : int):
        if depth == 0 or root.final():
            return root.eval(), None

        optVal = minOrMax * -100000
        optOp = None

        for op in root.ops():
            new = root.apply(op)

            val, dummy = self.alphabeta(new, depth - 1, -minOrMax, optVal)

            if val * minOrMax > optVal * minOrMax:
                optVal, optOp = val, op

                if optVal * minOrMax > parentValue * minOrMax:
                    break
        
        return optVal, optOp


class State:
    def __init__(self, game : OthelloGame):
        self.game = game

    def eval(self) -> int:
        factor = self.game.get_scores()[0]
        w, h = self.game.get_rows(), self.game.get_columns()
        center_x = round(w / 2)
        center_y = round(h / 2)

        for x, y in self.ops():
            shifted_x = x - center_x
            shifted_y = y - center_y

            # Prioritize side cells
            factor += abs(center_x - x) + abs(center_y - y)

            # Prioritize corners
            if x == 0 or x == w or y == 0 or y == h:
                factor += 10

        board = self.game.get_board()

        for x in range(0, w):
            for y in range(0, h):
                if board[x][y] == 'B':
                    factor += State.get_cell_score(x, y, w, h)

        # print("factor : " + str(factor))
            
        return factor # * self.game.get_scores()[0]

    def final(self):
        return self.game.is_game_over()

    @staticmethod
    def get_cell_score(x, y, w, h):
        bonus = 20
        score = 0
        if x == 0 and y == 0:
            score += bonus

        if x == 0 and y == h:
            score += bonus

        if x == w and y == 0:
            score += bonus

        if x == w and y == h:
            score += bonus

        return score

    
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


    

