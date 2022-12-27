''' Example of a random AI. The class name has to be the same as the module name.
'''

from __future__ import annotations
from copy import deepcopy # postpones the evaluation of the type hints, hence they do not need to be imported
import random
from othello import OthelloGame, NONE, BLACK, WHITE
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

        eval, move = self.alphabeta(State(game, debug = False), 3, 1, 0)

        return move

    def alphabeta(self, root : State, depth : int, minOrMax : int, parentValue : int):
        if depth == 0 or root.final():
            return root.eval(), None

        optVal = minOrMax * -sys.maxsize
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
    def __init__(self, game : OthelloGame, debug : bool = False):
        self.game = game
        self.debug = debug

    def eval(self) -> int:
        mobility = self.get_mobility_score(self.game)
        coin_parity = self.get_coin_parity_score(self.game)
        stability = self.get_stability_score(self.game)
        corner_captured = self.get_corner_captures_score(self.game)
        
        score = mobility + coin_parity + stability + corner_captured
        
        if self.debug:
            print("--------------------")
            # print(self.game.get_board())
            print(self.game.get_turn())
            [print(row) for row in self.game.get_board()]
            print("Mobility: ", mobility)
            print("Coin parity: ", coin_parity)
            print("Stability: ", stability)
            print("Corner captured: ", corner_captured)
            print("Score: ", score)
            print("--------------------\n")

        return score

    def final(self):
        return self.game.is_game_over()

    # Return a list boards with every legal move applied to the current board
    def ops(self) -> list[tuple[int, int]]:
        return self.game.get_possible_move()

    def apply(self, op : list[list[str]]) -> ThePension:
        new_game = self.game.copy_game()

        row, col = op

        new_game.move(row, col, False)

        return State(new_game, self.debug)
    
    @staticmethod
    def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    @staticmethod
    def get_mobility_score(game : OthelloGame):
        min_player_moves = len(game.get_possible_move())
        max_player_moves = len(State.get_possible_move(game, State.get_opponent(game)))
        
        # print("Max player moves: ", max_player_moves)
        # print("Min player moves: ", min_player_moves)
        
        if max_player_moves + min_player_moves != 0:
            return 100 * (max_player_moves - min_player_moves) / (max_player_moves + min_player_moves)
        else:
            return 0
    
    @staticmethod
    def get_coin_parity_score(game : OthelloGame):
        scores = game.get_scores()
        
        if game.get_turn() == 'W':
            return 100 * (scores[0] - scores[1]) / (scores[0] + scores[1])
        elif game.get_turn() == 'B':
            return 100 * (scores[1] - scores[0]) / (scores[1] + scores[0])
        
        print("Error: get_coin_parity_score")
    
    @staticmethod
    def get_stability_score(game : OthelloGame):
        max_player_stability_value = 0
        min_player_stability_value = 0
        board = game.get_board()
        
        cells_score = [
            [ 4, -3,  2,  2,  2,  2, -3,  4],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [ 2, -1,  1,  0,  0,  1, -1,  2],
            [ 2, -1,  0,  1,  1,  0, -1,  2],
            [ 2, -1,  0,  1,  1,  0, -1,  2],
            [ 2, -1,  1,  0,  0,  1, -1,  2],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [ 4, -3,  2,  2,  2,  2, -3,  4],
        ]
        
        for x in range(0, game.get_rows()):
            for y in range(0, game.get_columns()):
                if board[x][y] == game.get_turn():
                    max_player_stability_value += cells_score[x][y]
                elif board[x][y] == State.get_opponent(game):
                    min_player_stability_value += cells_score[x][y]
        
        return min_player_stability_value - max_player_stability_value
    
    @staticmethod
    def get_corner_captures_score(game : OthelloGame):
        max_player_corner_value = 0
        min_player_corner_value = 0
        
        # Check top left corner
        if game.get_board()[0][0] == game.get_turn():
            max_player_corner_value += 1
        elif game.get_board()[0][0] == State.get_opponent(game):
            min_player_corner_value += 1
            
        # Check top right corner
        if game.get_board()[0][game.get_columns() - 1] == game.get_turn():
            max_player_corner_value += 1
        elif game.get_board()[0][game.get_columns() - 1] == State.get_opponent(game):
            min_player_corner_value += 1
            
        # Check bottom left corner
        if game.get_board()[game.get_rows() - 1][0] == game.get_turn():
            max_player_corner_value += 1
        elif game.get_board()[game.get_rows() - 1][0] == State.get_opponent(game):
            min_player_corner_value += 1
            
        # Check bottom right corner
        if game.get_board()[game.get_rows() - 1][game.get_columns() - 1] == game.get_turn():
            max_player_corner_value += 1
        elif game.get_board()[game.get_rows() - 1][game.get_columns() - 1] == State.get_opponent(game):
            min_player_corner_value += 1
            
        min_player_corner_value, max_player_corner_value = max_player_corner_value, min_player_corner_value
        
        if max_player_corner_value + min_player_corner_value != 0:
            return 100 * (max_player_corner_value - min_player_corner_value) / (max_player_corner_value + min_player_corner_value)
        else:
            return 0
        
    @staticmethod
    def get_possible_move(game : OthelloGame, turn : str) -> list[tuple[int, int]]:
        """ Looks at all the empty cells in the board and return possible moves """
        possible_move = []
        for row in range(game.get_rows()):
            for col in range(game.get_columns()):
                if game._cell_color(row, col) == NONE:
                    possible_directions = game._adjacent_opposite_color_directions(row, col, turn)
                    for direction in possible_directions:
                        if game._is_valid_directional_move(row, col, direction[0], direction[1], turn):
                            possible_move.append((row, col))
        return possible_move
    
    @staticmethod
    def get_opponent(game : OthelloGame) -> str:
        if game.get_turn() == 'B':
            return 'W'
        else:
            return 'B'

    

