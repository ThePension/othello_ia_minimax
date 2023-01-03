''' This is the main file for the Othello game. It creates the game and the GUI and starts the game.
'''

import importlib
import threading
import othello
import othello_models_no_gui

# Default / Initial Game Settings
DEFAULT_ROWS = 7
DEFAULT_COLUMNS = 9

class OthelloNoGUI:
    def __init__(self):
        # Initial Game Settings
        self._rows = DEFAULT_ROWS
        self._columns = DEFAULT_COLUMNS
        self._black_name = "ThePension"
        self._white_name = "Random"
        self._white_ai = None
        self._black_ai = None

        # Create my othello gamestate here (drawn from the original othello game code)
        self._game_state = othello.OthelloGame(self._rows, self._columns, othello.BLACK)

        # Initialize all my widgets and window here
        self._black_player = othello_models_no_gui.Player(self._black_name)
        self._white_player = othello_models_no_gui.Player(self._white_name)
        self._board = othello_models_no_gui.GameBoard(self._game_state)
        self._black_score = othello_models_no_gui.Score(othello.BLACK, self._game_state)
        self._white_score = othello_models_no_gui.Score(othello.WHITE, self._game_state)
        self._player_turn = othello_models_no_gui.Turn(self._game_state)    
        
    def _new_game(self) -> None:
        ''' Creates a new game with current _game_state settings '''
        self._game_state = othello.OthelloGame(self._rows, self._columns,
                                               othello.BLACK)
        self._board.new_game_settings(self._game_state)
        self._black_score.update_score(self._game_state)
        self._white_score.update_score(self._game_state)
        self._player_turn.update_turn(self._game_state.get_turn())

        self._white_ai = getattr(importlib.import_module(f"ai.{self._white_name}"), f"{self._white_name}")()
        self._black_ai = getattr(importlib.import_module(f"ai.{self._black_name}"), f"{self._black_name}")()
        return self._play_ai()

    def _play(self, row, col):
        self._game_state.move(row, col)
        self._board.update_game_state(self._game_state)
        self._black_score.update_score(self._game_state)
        self._white_score.update_score(self._game_state)

        if self._game_state.is_game_over():
            return self._game_state.return_winner() 
        else:
            self._player_turn.switch_turn(self._game_state)
            return self._play_ai()

    def _play_ai(self):
        ''' Plays an AI move '''
        if self._game_state.get_turn() == othello.BLACK and self._black_ai is not None:
            move = self._black_ai.next_move(self._game_state.copy_game())
            return self._play(move[0], move[1])
        elif self._game_state.get_turn() == othello.WHITE and self._white_ai is not None:
            move = self._white_ai.next_move(self._game_state.copy_game())
            return self._play(move[0], move[1])


if __name__ == '__main__':
    print(OthelloNoGUI()._new_game())
