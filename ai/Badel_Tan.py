import random
from othello import OthelloGame
from math import inf

MAX_DEPTH = 5

class Badel_Tan:
    def __init__(self):
        pass

    def __str__(self):
        return "Badel_Tan"

    def next_move(self, board: OthelloGame) -> tuple[int, int]:
        """Returns the next move to play.

        Args:
            board (othello.OthelloGame): _description_

        Returns:
            tuple[int, int]: the next move (for instance: (2, 3) for (row, column), starting from 0)
        """

        dummy, move = minimax(board, 3, 1)
        return move
    

def minimax(root, depth, minOrMax):
    if depth == 0 or root.is_game_over():
        return eval(root), None
    
    optVal = minOrMax * -inf
    optOp = None
    
    for op in root.get_possible_move():
        new = root_apply(root, op)
        
        val, dummy = minimax(new, depth - 1, -minOrMax)
        
        if val * minOrMax > optVal * minOrMax:
            optVal = val
            optOp = op
            
    return optVal, optOp
        
        
def eval(root : OthelloGame) -> int:
    # TODO
    return 1

def root_apply(root : OthelloGame, op : tuple[int, int]) -> OthelloGame:
    new_game = root.copy_game()

    new_game.move(op[0], op[1], False)

    return new_game